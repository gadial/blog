# Quick Start Guide

## Setup (One-time)

1. **Install dependencies**:
```powershell
pip install -r requirements.txt
```

2. **Verify installation**:
```powershell
python build.py
```

You should see output confirming 1 post was generated.

## Daily Workflow

### Creating a New Post

1. Create a new markdown file in `content/posts/`:
```powershell
New-Item "content\posts\$(Get-Date -Format 'yyyy-MM-dd')-my-post.md"
```

2. Add frontmatter and content:
```markdown
---
title: "כותרת הפוסט"
date: 2025-11-28
categories:
  - מתמטיקה
tags:
  - נושא
---

תוכן הפוסט כאן...
```

3. Generate the HTML:
```powershell
python build.py
```

4. Preview in browser:
```powershell
Start-Process "output\$(Get-Date -Format 'yyyy-MM-dd')-my-post.html"
```

### Regenerating All Posts

```powershell
python build.py
```

### Generating a Single Post

```powershell
python build.py content\posts\2025-11-28-my-post.md
```

## Math Syntax

- **Inline**: `$x^2 + y^2 = r^2$`
- **Display**: `$$\int_0^\infty e^{-x^2} dx = \frac{\sqrt{\pi}}{2}$$`

## Code Blocks

````markdown
```python
def factorial(n):
    return 1 if n <= 1 else n * factorial(n-1)
```
````

## Project Structure at a Glance

```
new_blog/
├── build.py              ← Run this to generate
├── content/posts/        ← Put your .md files here
├── templates/post.html   ← Customize layout here
└── output/               ← Generated HTML appears here
```

## Testing the Sample Post

The project includes a sample post about quadratic equations. View it:

```powershell
Start-Process "output\2025-11-28-quadratic-equation.html"
```

## Customization

### Change the template

Edit `templates/post.html` to modify:
- Colors and fonts
- Layout structure
- Header/footer content

### Change math rendering

The template uses KaTeX. To switch to MathJax, edit the `<head>` section in `templates/post.html`.

### Add more markdown features

Edit `generator/markdown_processor.py` to add more Python-Markdown extensions.

## Troubleshooting

### Import errors
Make sure dependencies are installed:
```powershell
pip install -r requirements.txt
```

### Math not rendering
Check browser console for KaTeX errors. Ensure internet connection for CDN.

### Hebrew text not right-to-left
Verify `dir="rtl"` is set in the HTML template.

## Next Steps for Full Migration

1. Copy all posts from `c:\Users\gadia\Dropbox\Websites\blog\_posts\` to `content/posts/`
2. Test generation: `python build.py`
3. Review generated HTML files in `output/`
4. Customize `templates/post.html` to match your blog's style
5. Add index page generation (see README for future enhancements)
