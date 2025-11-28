# Site Configuration
# This file can be extended to include site-wide settings

SITE_CONFIG = {
    'title': 'בלוג מתמטיקה',
    'description': 'בלוג מתמטיקה בעברית',
    'language': 'he',
    'direction': 'rtl',
    'author': '',
    'base_url': '',
    
    # Paths
    'content_dir': 'content',
    'template_dir': 'templates',
    'output_dir': 'docs',
    'static_dir': 'static',
    
    # URL structure
    'use_date_folders': True,  # Creates /YYYY/MM/DD/slug/ structure
    'post_images': '/img',  # Path for {{site.post_images}}
    
    # Features
    'math_renderer': 'katex',  # or 'mathjax'
    'syntax_highlighting': True,
    'generate_index': False,  # Future feature
    'generate_categories': False,  # Future feature
    'generate_tags': False,  # Future feature
    'generate_rss': False,  # Future feature
}
