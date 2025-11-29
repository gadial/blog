# GitHub Pages Deployment Guide

## Quick Start

Your site is ready to deploy! Here's what to do:

### 1. Create GitHub Repository

1. Go to https://github.com/new
2. Repository name: `new_blog` (or any name you prefer)
3. Description: "Hebrew Mathematics Blog - Static Site"
4. **Public** repository (required for free GitHub Pages)
5. **Do NOT** initialize with README, .gitignore, or license
6. Click "Create repository"

### 2. Push Your Code

Run these commands in PowerShell:

```powershell
# Add the remote (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/new_blog.git

# Push your code
git push -u origin master
```

### 3. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings** (top menu)
3. Click **Pages** (left sidebar)
4. Under "Build and deployment":
   - Source: **Deploy from a branch**
   - Branch: **master**
   - Folder: **/docs**
5. Click **Save**

### 4. Wait for Deployment

- GitHub will build your site (takes 1-3 minutes)
- Look for a green checkmark in the "Actions" tab
- Your site will be available at: `https://YOUR_USERNAME.github.io/new_blog/`

### 5. Access Your Site

Once deployed, your site will be at:
- Full URL: `https://YOUR_USERNAME.github.io/new_blog/`
- All pages work because of the `/new_site` baseurl configuration

## Setting Up gadial.net/new_site

To make your site accessible at https://gadial.net/new_site, you have two options:

### Option A: Subdomain (Easiest)

1. **In your DNS settings** (where gadial.net is hosted):
   - Add a CNAME record:
     - Name: `newsite` or `new-site`
     - Value: `YOUR_USERNAME.github.io`
     - TTL: 3600

2. **Update config.py**:
   ```python
   'baseurl': '',  # Change from '/new_site' to empty string
   ```

3. **Rebuild and push**:
   ```powershell
   python build.py
   git add -A
   git commit -m "Update for subdomain"
   git push
   ```

4. **In GitHub repository Settings → Pages**:
   - Custom domain: `newsite.gadial.net`
   - Wait for DNS check to pass
   - Enable "Enforce HTTPS"

Your site will be at: `https://newsite.gadial.net`

### Option B: Proxy/Redirect (Advanced)

If you control the web server for gadial.net, set up a reverse proxy or redirect:

**Apache (.htaccess)**:
```apache
RewriteEngine On
RewriteRule ^new_site/(.*)$ https://YOUR_USERNAME.github.io/new_blog/$1 [P,L]
```

**Nginx**:
```nginx
location /new_site/ {
    proxy_pass https://YOUR_USERNAME.github.io/new_blog/;
    proxy_set_header Host YOUR_USERNAME.github.io;
}
```

This keeps the `/new_site` path and doesn't require changing baseurl.

## Testing Locally

Before pushing, always test locally:

```powershell
python serve.py
```

Visit: http://localhost:8000/new_site/

## Updating Content

To add or modify posts:

1. **Edit files** in `content/posts/`
2. **Rebuild**: `python build.py`
3. **Test**: `python serve.py`
4. **Deploy**:
   ```powershell
   git add -A
   git commit -m "Add new post about [topic]"
   git push
   ```

GitHub Pages automatically rebuilds within 1-3 minutes.

## Troubleshooting

### Site Shows 404
- Check Settings → Pages shows "Your site is published at..."
- Verify branch is "master" and folder is "/docs"
- Wait 5 minutes for DNS propagation

### Links Don't Work
- Check that config.py has correct `baseurl`
- Verify all templates use `{{ baseurl }}` prefix
- Rebuild: `python build.py`

### Math Not Rendering
- Check browser console for KaTeX errors
- Verify .nojekyll file exists in docs/
- Check that equations use $ or $$ delimiters

### Custom Domain Not Working
- DNS changes take 24-48 hours to propagate fully
- Use `nslookup newsite.gadial.net` to check DNS
- GitHub DNS check must pass before HTTPS works

## Files Changed for GitHub Pages

These files were configured for deployment:

1. **config.py**: Added `baseurl: '/new_site'`
2. **generator/site_generator.py**: Pass baseurl to all templates
3. **templates/**: All links use `{{ baseurl }}` prefix
4. **docs/.nojekyll**: Prevents Jekyll processing
5. **.github/workflows/deploy.yml**: Auto-deploy on push (optional)
6. **README.md**: Updated with deployment instructions

## Current Configuration

- **Output directory**: `docs/` (required by GitHub Pages)
- **Base URL**: `/new_site` (change if using custom domain)
- **Content**: 654 posts from 2007-2025
- **Math rendering**: KaTeX via CDN
- **Language**: Hebrew (RTL)

Your site is ready to go live! 🚀
