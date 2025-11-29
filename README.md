# Python Static Site Generator for Hebrew Math Blog

A lightweight Python-based static site generator designed to replace Jekyll for a Hebrew mathematics blog. Built with support for RTL text, LaTeX math rendering, and YAML frontmatter.

**Live Site**: https://gadial.net/new_site (GitHub Pages deployment)

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

### Local Development Build

For local testing (without baseurl prefix):

```powershell
python build_local.py
python serve.py
# Visit: http://localhost:8000/
```

### Production Build (for GitHub Pages)

To generate HTML with `/new_blog` baseurl:

```powershell
python build.py
```

This will:
- Clean the `docs/` directory
- Process all `.md` files in `content/`
- Generate HTML with baseurl prefix for GitHub Pages

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

## GitHub Pages Deployment

This site is configured to be deployed at https://gadial.net/new_site

### Initial Setup

1. **Create a new GitHub repository** (e.g., `new_blog`):
   ```bash
   # On GitHub.com, create a new repository
   ```

2. **Add remote and push**:
   ```powershell
   git remote add origin https://github.com/YOUR_USERNAME/new_blog.git
   git branch -M master
   git push -u origin master
   ```

3. **Configure GitHub Pages**:
   - Go to repository **Settings** → **Pages**
   - **Source**: Deploy from a branch
   - **Branch**: `master` (or `main`)
   - **Folder**: `/docs`
   - Click **Save**

4. **Wait** a few minutes for GitHub Pages to build and deploy

Your site will be available at: `https://YOUR_USERNAME.github.io/new_blog/`

### Custom Domain Setup (for gadial.net/new_site)

Since you want the new blog at https://gadial.net/new_site while keeping the old blog at https://gadial.net:

**Option 1: Subdirectory on same domain (Recommended)**
- Keep your old `blog` repository serving https://gadial.net
- Create this `new_blog` repository
- Configure it with `baseurl: '/new_site'` (already done in `config.py`)
- In your web hosting/DNS, set up a redirect or proxy from `/new_site` to the GitHub Pages URL

**Option 2: Use GitHub organization**
- Create a GitHub organization named after your domain
- This allows multiple repos to serve different paths
- More complex setup but cleaner URL structure

### Configuration

The site is already configured with:
- `baseurl: '/new_site'` in `config.py`
- All links use `{{ baseurl }}` prefix in templates
- `.nojekyll` file to prevent Jekyll processing

### Updating Content

After making changes:

```powershell
python build.py           # Rebuild the site
git add -A                # Stage all changes
git commit -m "Update content"
git push                  # Deploy to GitHub Pages
```

GitHub Pages will automatically update your site within a few minutes.

## License

© All rights reserved to Gadi Aleksandrowicz

## Next Steps

- [x] Index page generation
- [x] Post list with search
- [x] Random post page
- [x] Asset copying (images, CSS, JS)
- [x] Navigation (prev/next, top bar)
- [x] Math rendering (KaTeX)
- [ ] Category/tag pages
- [ ] RSS feed generation
- [ ] Watch mode for development
- [ ] Add pagination support
