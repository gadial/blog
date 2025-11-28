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
        
        # Initialize Jinja2 environment
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            autoescape=True
        )
        
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
                'url': f"/{prev_post.date.strftime('%Y/%m/%d')}/{prev_post.slug}/"
            }
        
        next_data = None
        if next_post:
            next_data = {
                'title': next_post.title,
                'url': f"/{next_post.date.strftime('%Y/%m/%d')}/{next_post.slug}/"
            }
        
        return template.render(
            post=post.to_dict(),
            prev_post=prev_data,
            next_post=next_data
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
        posts_data = []
        for post in sorted_posts:
            url = f"/{post.date.strftime('%Y/%m/%d')}/{post.slug}/"
            posts_data.append({
                'title': post.title,
                'date': post.date.strftime('%Y-%m-%d'),
                'categories': post.categories,
                'url': url,
                'summary': post.metadata.get('description', '')  # Use description from frontmatter
            })
        
        # Render index template
        template = self.jinja_env.get_template('index.html')
        html = template.render(posts=posts_data)
        
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
            url = f"/{post.date.strftime('%Y/%m/%d')}/{post.slug}/"
            posts_data.append({
                'title': post.title,
                'date': post.date.strftime('%Y-%m-%d'),
                'categories': post.categories,
                'url': url
            })
        
        # Render template
        template = self.jinja_env.get_template('post_list.html')
        html = template.render(posts=posts_data)
        
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
            url = f"/{post.date.strftime('%Y/%m/%d')}/{post.slug}/"
            posts_data.append({'url': url})
        
        posts_json = json.dumps(posts_data)
        
        # Render template
        template = self.jinja_env.get_template('random.html')
        html = template.render(posts_json=posts_json)
        
        # Save
        output_file = self.output_dir / 'random.html'
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        self.generation_log.append("Generated: random.html")
    
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
    
    # Load configuration
    try:
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
    
    # Check if a specific file was provided
    if len(sys.argv) > 1:
        post_file = Path(sys.argv[1])
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
