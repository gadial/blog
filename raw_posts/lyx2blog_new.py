#!/usr/bin/env python3
from pathlib import Path
import re
from datetime import datetime
from TexSoup import TexSoup, TexNode

front_matter_regex = r'\\title{(.*\n?.*)}\n\\maketitle\n\\begin{description}\n\\item \[{קטגוריות:}\] (.*)\n\\item \[{תגים:}\] (.*)\n\\item \[{מזהה:}\] \\L{(.*)}\n\\end{description}'
FRONT_RGX = re.compile(
    r'\\title{(?P<title>.*?)}.*?\n'
    r'\\maketitle.*?\n'
    r'\\begin{description}.*?\n'
    r'\\item\s*\[{קטגוריות:}\]\s*(?P<cats>.*?)\s*\n'
    r'\\item\s*\[{תגים:}\]\s*(?P<tags>.*?)\s*\n'
    r'\\item\s*\[{מזהה:}\]\s*\\L{(?P<id>.*?)}\n'
    r'\\end{description}',
)
SKIP_CMDS = ['documentclass', 'usepackage', 'selectlanguage']
SKIP_TAGS = ['document', 'L']
SKIP_SPACE_AFTER = ['textquotedblleft']
_pending_skip = False # global flag to skip the next blank line after a quote

_HEB_RE  = re.compile(r'[\u0590-\u05FF\uFB1D-\uFB4F]')   # Hebrew + presentation
_LAT_RE  = re.compile(r'[A-Za-z]')                       # plain Latin letters

def is_mostly_hebrew(text: str, ratio: float = 1.2) -> bool:
    """
    Return True if `text` contains noticeably more Hebrew than Latin letters.
    `ratio` is a tolerance factor: hebrew_count > ratio * latin_count.
    """
    heb = len(_HEB_RE.findall(text))
    lat = len(_LAT_RE.findall(text))
    return heb > ratio * lat

def extract_front(tex: str) -> tuple[str, dict]:
    m = FRONT_RGX.search(tex)
    if not m:
        raise ValueError("front-matter block not found")
    fm = {
        "title": m["title"].strip(),
        "categories": [c.strip() for c in m["cats"].split(",")],
        "tags":       [t.strip() for t in m["tags"].split(",")],
        "identifier": re.sub(r'\\','',m["id"]).strip()
    }
    tex = FRONT_RGX.sub("", tex, count=1)
    return tex, fm

def front_yaml(meta: dict) -> str:
    out = ["---",
           f'title: "{parentheses_fix(meta["title"])}"',
           "layout: post",
           "categories:"]
    out += [f"  - {c}" for c in meta["categories"]]
    out.append("tags:")
    out += [f"  - {t}" for t in meta["tags"]]
    out.append("---\n")
    return "\n".join(out)

def node_inner_text(node: TexNode) -> str:
    """Get the inner text of a TexSoup node, excluding any child nodes."""
    if isinstance(node, str):
        return node
    return ''.join(str(c) for c in node.contents if isinstance(c, str))

def parentheses_fix(text):  # relies on the fact that parentheses in mathmode are of the form \left( and \right)
    replacement = {'(': ')', ')': '('}
    return re.sub(r'(?<!\\left)\(|(?<!\\right)\)', lambda s: replacement.get(s.group(0), s.group(0)), text)

def emit(node: TexNode) -> str:
    """Recursively convert a TexSoup node to Markdown."""
    global _pending_skip
    if _pending_skip:
        _pending_skip = False
        if isinstance(node, str) and node[0].isspace():
            return node[1:]
        if str(node).isspace():              # TokenWithPosition case
            return ''
    # print("Processing node:", node)
    if isinstance(node, str):
        return parentheses_fix(node)
    
    if node.name in SKIP_TAGS:
        return f'{"".join(map(emit, node))}'
    if node.name in {"section", "section*"}:
        # return f'<h2>{node.string}</h2>'
        return f'## {node.string}'
    if node.name in {"subsection", "subsection*"}:
        return f'\n\n### {"".join(map(emit, node))}\n\n'
    if node.name in {"paragraph", "paragraph*"}:
        return f'\n\n#### {"".join(map(emit, node))}\n\n'
    if node.name == "textbf":
        return f'**{"".join(map(emit, node))}**'
    if node.name in {"textquotedblleft", "textquotedblright", "textquotedbl"}:
        if node.name in SKIP_SPACE_AFTER:
            _pending_skip = True             # eat the very next blank
        return '"'                           # emit the actual quote

    if node.name == "href":
        url = node.args[0].string
        text = node.args[1].string
        return f'[{text}]({url})'
    if node.name == "itemize":
        items = [f"- {''.join(map(emit, it))}" for it in node.children if it.name == "item"]
        return "\n".join(items) + "\n"
    if node.name == "enumerate":
        items = [f"1. {''.join(map(emit, it))}" for it in node.children if it.name == "item"]
        return "\n".join(items) + "\n"
    # 4. verbatim* or minted
    if node.name in {"verbatim*", "minted"}:
        lang = "python"
        body = node_inner_text(node)
        return f"{{% highlight {lang} %}}{body}{{% endhighlight %}}\n"
    # 5. math – keep delimiters
    if node.name in {"$", "$$"}:
        body = str(node).replace(node.name, '').strip()
        return f"{{% equation %}}{body}{{% endequation %}}"
    if node.name == "quote":
        body = ''.join(map(emit, node))
        if is_mostly_hebrew(body):
            dir = "rtl"
        else:
            dir = "ltr"
        return f"{{% quote {dir} %}}{body}{{% endquote %}}\n"
    if node.name in SKIP_CMDS:
        print("Skipping command:", node.name, "with args:", node.args)
        return ''
    # 6. unknown or inline commands – fall back to their LaTeX form
    print("Unknown node:", node.name, "with args:", node.args)
    return str(node.expr)

def convert(path: Path, out_dir: Path | None = None) -> Path:
    tex = path.read_text(encoding="utf-8")
    tex, meta = extract_front(tex)
    #tex = re.sub(r'(?m)^\s*%%.*$', '', tex)
    tex = re.sub(r'(?m)^\s*\\selectlanguage\{[^}]+\}%\s*$', '', tex)
    tex = re.sub(r'\{\\beginL\s*(.*?)\s*\\endL\}',lambda m: m.group(1), tex, flags=re.S)
    soup = TexSoup(tex)

    md_parts = [front_yaml(meta)]
    for child in soup:
        md_parts.append(emit(child))

    out_name = f'{datetime.now():%Y-%m-%d}-{meta["identifier"]}.md'
    out_path = (out_dir or path.parent) / out_name
    out_path.write_text("".join(md_parts), encoding="utf-8")
    return out_path

if __name__ == "__main__":
    import argparse, sys
    ap = argparse.ArgumentParser()
    ap.add_argument("texfile", type=Path)
    ap.add_argument("-o", "--outdir", type=Path)
    args = ap.parse_args()

    try:
        md = convert(args.texfile, args.outdir)
        print("✓ Wrote", md)
    except Exception as e:
        print("Error:", e, file=sys.stderr)
        sys.exit(1)
