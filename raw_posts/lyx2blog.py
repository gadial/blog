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
    r'\\item\s*\[{תגים:}\]\s*(?P<tags>.*?)(?=\s*\n\s*\\item\s*\[{מזהה:}\])'
    r'\s*\n\s*\\item\s*\[{מזהה:}\]\s*\\L{(?P<id>.*?)}\n'
    r'\\end{description}',
    re.DOTALL
)
SKIP_CMDS = ['documentclass', 'usepackage', 'selectlanguage']
SKIP_TAGS = ['document', 'L']
SKIP_SPACE_AFTER = ['textquotedblleft', 'textquotedblright', 'textquotedbl']
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
    
    # Clean up categories and tags: remove line breaks that don't start new \item
    # (in the frontmatter, any line break not starting with \item is a TeX mistake)
    cats_text = m["cats"]
    tags_text = m["tags"]
    
    # Replace newlines with spaces to join broken lines
    cats_text = re.sub(r'\s*\n\s*', ' ', cats_text)
    tags_text = re.sub(r'\s*\n\s*', ' ', tags_text)
    
    fm = {
        "title": m["title"].strip(),
        "categories": [c.strip() for c in cats_text.split(",")],
        "tags":       [t.strip() for t in tags_text.split(",")],
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
        return f'\n\n## {"".join(map(emit, node))}\n\n'
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
    if node.name == "includegraphics":
        # Extract the path from the arguments
        # Format: \includegraphics[scale=0.5]{path/to/image}
        img_path = str(node.args[-1]).strip('{}')  # Get the last arg (the path)
        # Extract year and filename from path
        # Path format: C:/Users/gadia/Dropbox/Websites/new_blog/static/img/2026/maze
        # We want: {{site.baseurl}}{{site.post_images}}/2026/maze.png
        parts = img_path.replace('\\', '/').split('/')
        # Find the year (4 digits) and filename after it
        for i, part in enumerate(parts):
            if part.isdigit() and len(part) == 4:
                year = part
                if i + 1 < len(parts):
                    filename = parts[i + 1]
                    # Add .png if no extension
                    if '.' not in filename:
                        filename += '.png'
                    return f'<img src="{{{{site.baseurl}}}}{{{{site.post_images}}}}/{year}/{filename}" alt=""/>\n\n'
        # Fallback if pattern doesn't match
        return f'<!-- Could not parse image path: {img_path} -->\n'
    if node.name == "itemize":
        items = [f"- {''.join(map(emit, it))}" for it in node.children if it.name == "item"]
        return "\n".join(items) + "\n"
    if node.name == "enumerate":
        items = [f"1. {''.join(map(emit, it))}" for it in node.children if it.name == "item"]
        return "\n".join(items) + "\n"
    # 4. verbatim* or minted or lstlisting
    if node.name in {"verbatim*", "minted"}:
        lang = "python"
        body = node_inner_text(node)
        return f"{{% highlight {lang} %}}{body}{{% endhighlight %}}\n"
    if node.name == "lstlisting":
        # For lstlisting, we need to preserve all braces, so use str() instead of node_inner_text()
        lang = "python"
        # Get the string representation and extract content between \begin{lstlisting} and \end{lstlisting}
        body_str = str(node)
        # Remove the \begin{lstlisting} and \end{lstlisting} markers
        body = re.sub(r'^\\begin\{lstlisting\}', '', body_str)
        body = re.sub(r'\\end\{lstlisting\}$', '', body)
        body = body.strip()
        return f"{{% highlight {lang} %}}\n{body}\n{{% endhighlight %}}\n"
    # 5. math – keep delimiters
    if node.name in {"$", "$$"}:
        body = str(node).replace(node.name, '').strip()
        # Replace < and > with \lt and \gt to avoid HTML parsing issues
        body = body.replace('<', r'\lt ').replace('>', r'\gt ')
        # Add newlines around display equations ($$) but space after inline ($)
        if node.name == "$$":
            return f"\n\n{{% equation %}}{body}{{% endequation %}}\n\n"
        else:
            return f"{{% equation %}}{body}{{% endequation %}} "
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
    # Try UTF-8 first, fall back to cp1255 (Hebrew Windows) or ignore errors
    try:
        tex = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        try:
            tex = path.read_text(encoding="cp1255")
        except UnicodeDecodeError:
            tex = path.read_text(encoding="utf-8", errors="ignore")
    tex, meta = extract_front(tex)
    #tex = re.sub(r'(?m)^\s*%%.*$', '', tex)
    tex = re.sub(r'(?m)^\s*\\selectlanguage\{[^}]+\}%\s*$', '', tex)
    tex = re.sub(r'\{\\beginL\s*(.*?)\s*\\endL\}',lambda m: m.group(1), tex, flags=re.S)
    soup = TexSoup(tex)

    md_parts = [front_yaml(meta)]
    for child in soup:
        md_parts.append(emit(child))

    # Join the markdown parts
    md_text = "".join(md_parts)
    
    # Split into frontmatter and content
    parts = md_text.split('---\n', 2)
    if len(parts) >= 3:
        frontmatter = '---\n' + parts[1] + '---\n'
        content = parts[2] if len(parts) > 2 else ''
    else:
        frontmatter = ''
        content = md_text
    
    # Process content: In TeX/LaTeX, single newlines are just whitespace, 
    # only double newlines (blank lines) create new paragraphs
    
    # First, normalize line endings in content
    content = content.replace('\r\n', '\n')
    
    # Remove LyX metadata junk at the beginning - only the comment lines and addto/renewcommand lines
    content = re.sub(r'^%%[^\n]*\n', '', content, flags=re.MULTILINE)  # Remove %% comment lines
    content = re.sub(r'^\\addto[^\n]*\n', '', content, flags=re.MULTILINE)  # Remove \addto lines
    content = re.sub(r'^\\renewcommand[^\n]*\n', '', content, flags=re.MULTILINE)  # Remove \renewcommand lines
    
    # Remove stray encoding/group commands that appear around code blocks
    content = re.sub(r'%?\\bgroup\\inputencoding\{[^}]+\}', '', content)
    content = re.sub(r'\\leavevmode\\egroup%?', '', content)
    
    # Normalize multiple blank lines to double newlines
    content = re.sub(r'\n\n+', '\n\n', content)
    
    # Ensure equations that are on separate lines in the source stay on separate lines
    # If we have endequation followed by whitespace and then equation, normalize to double newline
    content = re.sub(r'(\{%\s*endequation\s*%\})\s*(\{%\s*equation\s*%\})', r'\1\n\n\2', content)
    
    # TeX has linebreaks in the middle of paragraphs for no reason
    # Only double linebreaks (blank lines) are actual paragraph breaks
    # But we need to preserve linebreaks inside code blocks and protect equation blocks
    
    # First, extract code blocks and equation blocks, replacing them with placeholders
    protected_blocks = []
    def save_protected_block(match):
        protected_blocks.append(match.group(0))
        return f'___PROTECTED_BLOCK_{len(protected_blocks)-1}___'
    
    # Protect code blocks
    content = re.sub(r'\{%\s*highlight\s+\w+\s*%\}.*?\{%\s*endhighlight\s*%\}', 
                     save_protected_block, content, flags=re.DOTALL)
    
    # Protect equation blocks (to preserve any formatting/line breaks inside them)
    # Don't include trailing whitespace so inline equations can be joined with following text
    content = re.sub(r'\{%\s*equation\s*%\}.*?\{%\s*endequation\s*%\}', 
                     save_protected_block, content, flags=re.DOTALL)
    
    # Now replace single newlines with spaces while preserving double newlines
    content = re.sub(r'(?<!\n)\n(?!\n)', ' ', content)
    
    # Restore protected blocks
    for i, block in enumerate(protected_blocks):
        content = content.replace(f'___PROTECTED_BLOCK_{i}___', block)
    
    # Clean up multiple spaces
    content = re.sub(r' +', ' ', content)
    
    # Recombine frontmatter and content
    md_text = frontmatter + '\n' + content
    
    out_name = f'{datetime.now():%Y-%m-%d}-{meta["identifier"]}.md'
    out_path = (out_dir or path.parent) / out_name
    out_path.write_text(md_text, encoding="utf-8")
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
