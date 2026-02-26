"""Main static site generator module."""
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from generator.post import Post
from generator.markdown_processor import MarkdownProcessor
from generator.jekyll_compat import JekyllProcessor
import shutil
import sys
from datetime import datetime


class SiteGenerator:
    """Static site generator for Hebrew math blog."""
    
    def __init__(self, 
                 content_dir: str = 'content',
                 template_dir: str = 'templates',
                 output_dir: str = 'docs',
                 static_dir: str = 'static',
                 use_date_folders: bool = True,
                 site_config: dict = None):
        """Initialize the site generator.
        
        Args:
            content_dir: Directory containing markdown posts
            template_dir: Directory containing Jinja2 templates
            output_dir: Directory for generated HTML files
            static_dir: Directory for static assets (images, CSS, JS)
            use_date_folders: Whether to create /YYYY/MM/DD/slug/ structure
            site_config: Site configuration for Jekyll compatibility
        """
        self.content_dir = Path(content_dir)
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)
        self.static_dir = Path(static_dir)
        self.use_date_folders = use_date_folders
        self.site_config = site_config or {}
        self.baseurl = self.site_config.get('baseurl', '')
        
        # Initialize Jinja2 environment
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            autoescape=True
        )
        
        # Add custom filter for safe filenames
        import re as _re
        self.jinja_env.filters['safe_filename'] = lambda s: _re.sub(r'[<>:"/\\|?*]', '_', s)
        
        # Initialize markdown processor
        self.md_processor = MarkdownProcessor()
        
        # Initialize Jekyll compatibility processor
        self.jekyll_processor = JekyllProcessor(self.site_config)
        
        # Initialize log files
        self.generation_log = []
        self.warning_log = []
    
    def clean_output(self):
        """Remove all files from output directory."""
        if self.output_dir.exists():
            # Remove only HTML files to avoid issues with locked files
            for html_file in self.output_dir.rglob('*.html'):
                try:
                    html_file.unlink()
                except PermissionError:
                    print(f"Warning: Could not remove {html_file} (file may be open)")
        else:
            self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def copy_static_files(self):
        """Copy static files (images, CSS, JS) to output directory."""
        if not self.static_dir.exists():
            return
        
        print(f"Copying static files from {self.static_dir}...")
        
        # Copy entire static directory to output
        for item in self.static_dir.rglob('*'):
            if item.is_file():
                # Calculate relative path
                rel_path = item.relative_to(self.static_dir)
                dest_path = self.output_dir / rel_path
                
                # Create destination directory if needed
                dest_path.parent.mkdir(parents=True, exist_ok=True)
                
                # Copy file
                shutil.copy2(item, dest_path)
        
        print(f"Static files copied.")
    
    def process_post(self, post_file: Path) -> Post:
        """Process a single post file.
        
        Args:
            post_file: Path to the markdown post file
            
        Returns:
            Processed Post object
        """
        # Parse the post
        post = Post(post_file)
        
        # Set the post URL
        post.url = f"{self.baseurl}/{post.date.strftime('%Y/%m/%d')}/{post.slug}/"
        
        # Process Jekyll-specific syntax
        processed_content = self.jekyll_processor.process(post.content)
        
        # Convert markdown to HTML
        post.html_content = self.md_processor.process(processed_content)
        
        # Check for warnings from markdown processor
        warnings = self.md_processor.get_warnings()
        if warnings:
            for warning in warnings:
                self.warning_log.append(f"{post_file.name}: {warning}")
        
        return post
    
    def render_post(self, post: Post, prev_post=None, next_post=None) -> str:
        """Render a post using Jinja2 template.
        
        Args:
            post: Post object to render
            prev_post: Previous post (chronologically older)
            next_post: Next post (chronologically newer)
            
        Returns:
            Rendered HTML string
        """
        template = self.jinja_env.get_template('post.html')
        
        # Prepare prev/next post data
        prev_data = None
        if prev_post:
            prev_data = {
                'title': prev_post.title,
                'url': f"{self.baseurl}/{prev_post.date.strftime('%Y/%m/%d')}/{prev_post.slug}/"
            }
        
        next_data = None
        if next_post:
            next_data = {
                'title': next_post.title,
                'url': f"{self.baseurl}/{next_post.date.strftime('%Y/%m/%d')}/{next_post.slug}/"
            }
        
        return template.render(
            post=post.to_dict(),
            prev_post=prev_data,
            next_post=next_data,
            baseurl=self.baseurl
        )
    
    def get_output_path(self, post: Post) -> Path:
        """Generate output path for a post based on date and slug.
        
        Args:
            post: Post object
            
        Returns:
            Path object for the output HTML file
        """
        if self.use_date_folders:
            # Create /YYYY/MM/DD/slug/ structure like Jekyll
            year = post.date.strftime('%Y')
            month = post.date.strftime('%m')
            day = post.date.strftime('%d')
            
            # Create directory structure
            post_dir = self.output_dir / year / month / day / post.slug
            post_dir.mkdir(parents=True, exist_ok=True)
            
            # Return path to index.html inside the directory
            return post_dir / 'index.html'
        else:
            # Simple flat structure
            return self.output_dir / f"{post.slug}.html"
    
    def save_post(self, post: Post, html: str):
        """Save rendered HTML to output directory.
        
        Args:
            post: Post object
            html: Rendered HTML string
        """
        output_file = self.get_output_path(post)
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        # Log to file instead of printing
        rel_path = output_file.relative_to(self.output_dir)
        self.generation_log.append(f"Generated: {rel_path}")
    
    def generate_post(self, post_file: Path):
        """Process and generate HTML for a single post.
        
        Args:
            post_file: Path to the markdown post file
        """
        post = self.process_post(post_file)
        html = self.render_post(post)
        self.save_post(post, html)
    
    def generate_index(self, posts: list):
        """Generate index page with list of posts.
        
        Args:
            posts: List of Post objects to display
        """
        # Sort posts by date (newest first)
        sorted_posts = sorted(posts, key=lambda p: p.date, reverse=True)
        
        # Prepare post data for template
        all_posts_data = []
        for post in sorted_posts:
            url = f"{self.baseurl}/{post.date.strftime('%Y/%m/%d')}/{post.slug}/"
            all_posts_data.append({
                'title': post.title,
                'date': post.date.strftime('%Y-%m-%d'),
                'categories': post.categories,
                'url': url,
                'summary': post.metadata.get('description', '')  # Use description from frontmatter
            })
        
        # Get only the 5 latest posts for display
        latest_posts = all_posts_data[:5]
        
        # Render index template with both latest posts and all posts (for random selection)
        template = self.jinja_env.get_template('index.html')
        html = template.render(latest_posts=latest_posts, all_posts=all_posts_data, baseurl=self.baseurl)
        
        # Save index.html to root of output directory
        index_file = self.output_dir / 'index.html'
        with open(index_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        self.generation_log.append("Generated: index.html")
    
    def generate_post_list(self, posts: list):
        """Generate post list page with search.
        
        Args:
            posts: List of Post objects
        """
        # Sort posts by date (newest first)
        sorted_posts = sorted(posts, key=lambda p: p.date, reverse=True)
        
        # Prepare post data
        posts_data = []
        for post in sorted_posts:
            url = f"{self.baseurl}/{post.date.strftime('%Y/%m/%d')}/{post.slug}/"
            posts_data.append({
                'title': post.title,
                'date': post.date.strftime('%Y-%m-%d'),
                'categories': post.categories,
                'url': url
            })
        
        # Render template
        template = self.jinja_env.get_template('post_list.html')
        html = template.render(posts=posts_data, baseurl=self.baseurl)
        
        # Save
        output_file = self.output_dir / 'post_list.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        self.generation_log.append("Generated: post_list.html")
    
    def generate_random(self, posts: list):
        """Generate random post redirect page.
        
        Args:
            posts: List of Post objects
        """
        # Prepare post URLs as JSON
        import json
        posts_data = []
        for post in posts:
            url = f"{self.baseurl}/{post.date.strftime('%Y/%m/%d')}/{post.slug}/"
            posts_data.append({'url': url})
        
        posts_json = json.dumps(posts_data)
        
        # Render template
        template = self.jinja_env.get_template('random.html')
        html = template.render(posts_json=posts_json, baseurl=self.baseurl)
        
        # Save
        output_file = self.output_dir / 'random.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        self.generation_log.append("Generated: random.html")
    
    def generate_lecture_notes(self):
        """Generate lecture notes page."""
        template = self.jinja_env.get_template('lecture_notes.html')
        html = template.render(baseurl=self.baseurl)
        
        output_file = self.output_dir / 'lecture_notes.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        self.generation_log.append("Generated: lecture_notes.html")

    def generate_rss(self, posts: list, max_items: int = 20):
        """Generate RSS feed.
        
        Args:
            posts: List of Post objects
            max_items: Maximum number of items to include in feed
        """
        from email.utils import formatdate
        
        # Sort posts by date (newest first) and limit
        sorted_posts = sorted(posts, key=lambda p: p.date, reverse=True)[:max_items]
        
        # Prepare post data for RSS
        posts_data = []
        for post in sorted_posts:
            url = f"https://gadial.net/{post.date.strftime('%Y/%m/%d')}/{post.slug}/"
            posts_data.append({
                'title': post.title,
                'url': url,
                'pub_date': formatdate(post.date.timestamp(), localtime=False, usegmt=True),
                'excerpt': post.excerpt,
                'categories': post.categories
            })
        
        # Current date for lastBuildDate
        build_date = formatdate(datetime.now().timestamp(), localtime=False, usegmt=True)
        
        # Render template
        template = self.jinja_env.get_template('rss.xml')
        xml = template.render(posts=posts_data, build_date=build_date)
        
        # Save
        output_file = self.output_dir / 'feed.xml'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(xml)
        
        self.generation_log.append("Generated: feed.xml")
    
    def generate_categories(self, posts: list):
        """Generate category pages.
        
        Args:
            posts: List of Post objects
        """
        from collections import defaultdict
        from urllib.parse import quote
        
        # Build category index
        categories = defaultdict(list)
        for post in posts:
            for category in post.categories:
                url = f"{self.baseurl}/{post.date.strftime('%Y/%m/%d')}/{post.slug}/"
                categories[category].append({
                    'title': post.title,
                    'date': post.date.strftime('%Y-%m-%d'),
                    'url': url,
                    'summary': post.metadata.get('summary', '')
                })
        
        # Sort posts within each category by date (newest first)
        for category in categories:
            categories[category].sort(key=lambda p: p['date'], reverse=True)
        
        # Create categories directory in output
        categories_dir = self.output_dir / 'categories'
        categories_dir.mkdir(exist_ok=True)
        
        # Generate individual category pages
        template = self.jinja_env.get_template('category.html')
        for category, category_posts in categories.items():
            # URL encode the category name for the filename
            category_filename = f"{category}.html"
            
            html = template.render(
                category_name=category,
                posts=category_posts,
                post_count=len(category_posts),
                baseurl=self.baseurl
            )
            
            # Save category page
            output_file = categories_dir / category_filename
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)
            
            self.generation_log.append(f"Generated: categories/{category_filename}")
        
        # Generate categories index page
        categories_list = [
            {'name': cat, 'count': len(posts_list), 'url': f"{self.baseurl}/categories/{cat}.html"}
            for cat, posts_list in sorted(categories.items())
        ]
        
        template = self.jinja_env.get_template('categories.html')
        html = template.render(categories=categories_list, baseurl=self.baseurl)
        
        output_file = categories_dir / 'index.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        self.generation_log.append("Generated: categories/index.html")
    
    @staticmethod
    def _safe_filename(name) -> str:
        """Create a filesystem-safe filename from a name.
        
        Replaces characters that are invalid on Windows (< > : " / \\ | ? *)
        with underscores.
        """
        import re
        return re.sub(r'[<>:"/\\|?*]', '_', str(name))
    
    def generate_tags(self, posts: list):
        """Generate tag pages.
        
        Args:
            posts: List of Post objects
        """
        from collections import defaultdict
        
        # Build tag index
        tags = defaultdict(list)
        for post in posts:
            for tag in post.tags:
                url = f"{self.baseurl}/{post.date.strftime('%Y/%m/%d')}/{post.slug}/"
                tags[tag].append({
                    'title': post.title,
                    'date': post.date.strftime('%Y-%m-%d'),
                    'url': url,
                    'summary': post.metadata.get('summary', '')
                })
        
        # Sort posts within each tag by date (newest first)
        for tag in tags:
            tags[tag].sort(key=lambda p: p['date'], reverse=True)
        
        # Create tags directory in output
        tags_dir = self.output_dir / 'tags'
        tags_dir.mkdir(exist_ok=True)
        
        # Generate individual tag pages
        template = self.jinja_env.get_template('tag.html')
        for tag, tag_posts in tags.items():
            safe_tag = self._safe_filename(tag)
            tag_filename = f"{safe_tag}.html"
            
            html = template.render(
                tag_name=tag,
                posts=tag_posts,
                post_count=len(tag_posts),
                baseurl=self.baseurl
            )
            
            output_file = tags_dir / tag_filename
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(html)
            
            self.generation_log.append(f"Generated: tags/{tag_filename}")
        
        # Generate tags index page
        tags_list = [
            {'name': str(tag), 'count': len(posts_list), 'url': f"{self.baseurl}/tags/{self._safe_filename(tag)}.html"}
            for tag, posts_list in sorted(tags.items(), key=lambda x: str(x[0]))
        ]
        
        template = self.jinja_env.get_template('tags.html')
        html = template.render(tags=tags_list, baseurl=self.baseurl)
        
        output_file = tags_dir / 'index.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        self.generation_log.append("Generated: tags/index.html")
    
    def generate_all(self):
        """Generate HTML for all posts in content directory."""
        start_time = datetime.now()
        
        print("Starting site generation...")
        print(f"Content directory: {self.content_dir.absolute()}")
        print(f"Output directory: {self.output_dir.absolute()}")
        print()
        
        # Clean output directory
        self.clean_output()
        
        # Copy static files first
        self.copy_static_files()
        print()
        
        # Find all markdown files
        post_files = list(self.content_dir.glob('**/*.md'))
        
        if not post_files:
            print("No markdown files found in content directory.")
            return
        
        total_posts = len(post_files)
        print(f"Found {total_posts} post(s)")
        print()
        
        # Process each post and collect them (without rendering yet)
        processed_posts = []
        print("Processing posts: ", end='', flush=True)
        
        for i, post_file in enumerate(post_files, 1):
            try:
                post = self.process_post(post_file)
                processed_posts.append(post)
                
                # Update progress on same line
                percent = (i * 100) // total_posts
                sys.stdout.write(f'\rProcessing posts: {percent}% ({i}/{total_posts})')
                sys.stdout.flush()
                
            except Exception as e:
                error_msg = f"Error processing {post_file.name}: {e}"
                self.warning_log.append(error_msg)
        
        print()  # New line after progress
        
        # Sort posts by date for prev/next navigation
        sorted_posts = sorted(processed_posts, key=lambda p: p.date)
        
        # Now render and save with prev/next links
        print("Rendering posts: ", end='', flush=True)
        for i, post in enumerate(sorted_posts):
            try:
                prev_post = sorted_posts[i - 1] if i > 0 else None
                next_post = sorted_posts[i + 1] if i < len(sorted_posts) - 1 else None
                
                html = self.render_post(post, prev_post, next_post)
                self.save_post(post, html)
                
                # Update progress
                percent = ((i + 1) * 100) // total_posts
                sys.stdout.write(f'\rRendering posts: {percent}% ({i + 1}/{total_posts})')
                sys.stdout.flush()
                
            except Exception as e:
                error_msg = f"Error rendering {post.slug}: {e}"
                self.warning_log.append(error_msg)
        
        print()  # New line after progress
        print()
        
        # Generate special pages
        if processed_posts:
            print("Generating special pages...")
            self.generate_index(processed_posts)
            self.generate_post_list(processed_posts)
            self.generate_random(processed_posts)
            self.generate_lecture_notes()
            self.generate_rss(processed_posts)
            
            # Generate categories if enabled
            if self.site_config.get('generate_categories', False):
                print("Generating category pages...")
                self.generate_categories(processed_posts)
            
            # Generate tags if enabled
            if self.site_config.get('generate_tags', False):
                print("Generating tag pages...")
                self.generate_tags(processed_posts)
        
        print()
        
        # Write logs to files
        self._write_logs()
        
        # Calculate duration
        duration = datetime.now() - start_time
        
        print(f"Site generation complete!")
        print(f"  Posts generated: {len(processed_posts)}")
        print(f"  Warnings: {len(self.warning_log)}")
        print(f"  Duration: {duration.total_seconds():.1f}s")
        
        if self.warning_log:
            print(f"\nSee warnings.log for details")
    
    def generate_latest(self):
        """Generate only the latest post and update index page.
        
        This is useful for quick checks when working on the newest post.
        """
        start_time = datetime.now()
        
        # Find all post files
        post_files = sorted(self.content_dir.glob('posts/*.md'), reverse=True)
        
        if not post_files:
            print("No posts found.")
            return
        
        print("Quick build mode: Processing latest post only...")
        print()
        
        # Get the latest post file
        latest_file = post_files[0]
        
        # Process the latest post
        print(f"Processing: {latest_file.name}")
        latest_post = self.process_post(latest_file)
        
        # For navigation links, we need at least the previous post
        prev_post = None
        if len(post_files) > 1:
            prev_post = self.process_post(post_files[1])
        
        # Render and save the latest post
        html = self.render_post(latest_post, prev_post, None)
        self.save_post(latest_post, html)
        print(f"Generated: {latest_post.date.strftime('%Y/%m/%d')}/{latest_post.slug}/")
        print()
        
        # Process all posts for index (but don't render them all)
        print("Processing all posts for index...")
        all_posts = []
        for post_file in post_files:
            try:
                post = self.process_post(post_file)
                all_posts.append(post)
            except Exception as e:
                self.warning_log.append(f"Error processing {post_file.name} for index: {e}")
        
        # Generate index page
        print("Regenerating index page...")
        self.generate_index(all_posts)
        print()
        
        # Write logs
        self._write_logs()
        
        # Calculate duration
        duration = datetime.now() - start_time
        
        print(f"Quick build complete!")
        print(f"  Latest post: {latest_post.title}")
        print(f"  Duration: {duration.total_seconds():.1f}s")
        
        if self.warning_log:
            print(f"  Warnings: {len(self.warning_log)} (see warnings.log)")
    
    def _write_logs(self):
        """Write generation and warning logs to files."""
        # Write generation log
        with open('generation.log', 'w', encoding='utf-8') as f:
            f.write(f"Site generation log - {datetime.now()}\n")
            f.write("=" * 60 + "\n\n")
            for entry in self.generation_log:
                f.write(entry + "\n")
        
        # Write warnings log
        with open('warnings.log', 'w', encoding='utf-8') as f:
            f.write(f"Site generation warnings - {datetime.now()}\n")
            f.write("=" * 60 + "\n\n")
            if self.warning_log:
                for warning in self.warning_log:
                    f.write(warning + "\n")
            else:
                f.write("No warnings\n")


def main():
    """Main entry point for the generator."""
    import sys
    import os
    import argparse
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Generate static site from markdown posts')
    parser.add_argument('--latest', action='store_true',
                        help='Build only the latest post and regenerate index (fast)')
    parser.add_argument('file', nargs='?',
                        help='Build a specific post file')
    args = parser.parse_args()
    
    # Load configuration (use local config if USE_LOCAL_CONFIG env var is set)
    try:
        if os.environ.get('USE_LOCAL_CONFIG'):
            from config_local import LOCAL_CONFIG
            site_config = LOCAL_CONFIG
            print("Using local development configuration (baseurl='')...")
        else:
            from config import SITE_CONFIG
            site_config = SITE_CONFIG
    except ImportError:
        site_config = {}
    
    # Initialize generator with configuration
    generator = SiteGenerator(
        content_dir=site_config.get('content_dir', 'content'),
        template_dir=site_config.get('template_dir', 'templates'),
        output_dir=site_config.get('output_dir', 'docs'),
        static_dir=site_config.get('static_dir', 'static'),
        use_date_folders=site_config.get('use_date_folders', True),
        site_config=site_config
    )
    
    # Handle different build modes
    if args.latest:
        # Quick build: only latest post + index
        generator.generate_latest()
    elif args.file:
        # Build specific file
        post_file = Path(args.file)
        if post_file.exists():
            generator.generate_post(post_file)
        else:
            print(f"Error: File not found: {post_file}")
            sys.exit(1)
    else:
        # Generate all posts
        generator.generate_all()


if __name__ == '__main__':
    main()
