# Python Static Site Generator for Hebrew Math Blog

A lightweight Python-based static site generator designed to replace Jekyll for a Hebrew mathematics blog. Built with support for RTL text, LaTeX math rendering, and YAML frontmatter.

## Features

- ✅ **YAML Frontmatter**: Parse Jekyll-style metadata (title, date, categories, tags)
- ✅ **Markdown Processing**: Convert markdown to HTML with extended syntax support
- ✅ **Math Support**: Render LaTeX equations using KaTeX (inline: `$...$`, display: `$$...$$`)
- ✅ **RTL Hebrew Support**: Proper right-to-left layout and typography
- ✅ **Jinja2 Templates**: Flexible templating system
- ✅ **Syntax Highlighting**: Code block support with proper styling

## Project Structure

```
new_blog/
├── generator/              # Core generator code
│   ├── __init__.py
│   ├── post.py            # Post parser and frontmatter handler
│   ├── markdown_processor.py  # Markdown to HTML with math support
│   ├── jekyll_compat.py   # Jekyll compatibility layer
│   └── site_generator.py  # Main generator logic
├── templates/             # Jinja2 templates
│   └── post.html         # Post template with RTL styling
├── content/              # Your markdown posts
│   └── posts/
│       └── *.md          # Markdown files with frontmatter
├── static/               # Static assets (images, CSS, JS)
│   └── images/posts/     # Post images
├── docs/                 # Generated static HTML files (GitHub Pages)
├── build.py              # Build script
├── config.py             # Site configuration
└── requirements.txt      # Python dependencies
```

## Installation

1. **Create a Python virtual environment** (recommended):

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

2. **Install dependencies**:

```powershell
pip install -r requirements.txt
```

## Usage

### Generate All Posts

To generate HTML for all posts in the `content/` directory:

```powershell
python build.py
```

This will:
- Clean the `output/` directory
- Process all `.md` files in `content/`
- Generate corresponding `.html` files in `output/`

### Generate a Single Post

To generate HTML for a specific post:

```powershell
python build.py content\posts\2025-11-28-quadratic-equation.md
```

### View Generated Site

Open the generated HTML files in your browser:

```powershell
Start-Process output\2025-11-28-quadratic-equation.html
```

## Creating Posts

Posts are markdown files with YAML frontmatter. Create a new file in `content/posts/`:

```markdown
---
title: "כותרת הפוסט"
date: 2025-11-28
layout: post
categories:
  - אלגברה
  - גאומטריה
tags:
  - משוואות
  - פתרונות
---

# תוכן הפוסט

זהו פסקה בעברית עם משוואה: $x^2 + y^2 = r^2$

## משוואה מרכזית

$$\int_{-\infty}^{\infty} e^{-x^2} dx = \sqrt{\pi}$$

## קוד לדוגמה

\`\`\`python
def hello():
    print("שלום עולם")
\`\`\`
```

### Frontmatter Fields

- **title**: Post title (required)
- **date**: Publication date in `YYYY-MM-DD` format (required)
- **layout**: Template to use (default: `post`)
- **categories**: List of categories
- **tags**: List of tags

## Math Rendering

The generator uses KaTeX for fast, high-quality math rendering:

- **Inline math**: `$E = mc^2$` → $E = mc^2$
- **Display math**: `$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$`

Math expressions are automatically detected and wrapped for KaTeX rendering.

## Customization

### Templates

Edit `templates/post.html` to customize:
- Layout and styling
- Header/footer content
- Meta tags
- CSS/JavaScript includes

### Markdown Extensions

The generator uses Python-Markdown with these extensions:
- `extra`: Tables, footnotes, abbreviations
- `codehilite`: Syntax highlighting
- `fenced_code`: Code blocks with language specification
- `nl2br`: Convert newlines to `<br>` tags

To add more extensions, edit `generator/markdown_processor.py`.

### Output Structure

Currently, posts are generated as `{slug}.html` in the `output/` directory. To organize by date or categories, modify the `save_post()` method in `generator/site_generator.py`.

## Migration from Jekyll

To migrate your existing Jekyll blog:

1. Copy markdown files from `_posts/` to `content/posts/`
2. Ensure frontmatter uses YAML format (should be compatible)
3. Update any Jekyll-specific Liquid tags to plain markdown or HTML
4. Run the generator and verify output

## Development

### Running Tests

```powershell
python -m pytest tests/
```

### Adding Features

The generator is modular:
- **Post parsing**: `generator/post.py`
- **Markdown processing**: `generator/markdown_processor.py`
- **Template rendering**: `generator/site_generator.py`
- **Templates**: `templates/`

## Dependencies

- **Jinja2**: Template engine
- **Markdown**: Markdown to HTML conversion
- **python-frontmatter**: YAML frontmatter parsing
- **PyYAML**: YAML parsing
- **python-markdown-math**: Math extension support

## License

This generator is provided as-is for personal use.

## Next Steps

- [ ] Add index page generation
- [ ] Add category/tag pages
- [ ] Add RSS feed generation
- [ ] Add asset copying (images, CSS, JS)
- [ ] Add watch mode for development
- [ ] Add pagination support
