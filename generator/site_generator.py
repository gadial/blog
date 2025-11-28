"""Main static site generator module."""
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from generator.post import Post
from generator.markdown_processor import MarkdownProcessor
import shutil


class SiteGenerator:
    """Static site generator for Hebrew math blog."""
    
    def __init__(self, 
                 content_dir: str = 'content',
                 template_dir: str = 'templates',
                 output_dir: str = 'output'):
        """Initialize the site generator.
        
        Args:
            content_dir: Directory containing markdown posts
            template_dir: Directory containing Jinja2 templates
            output_dir: Directory for generated HTML files
        """
        self.content_dir = Path(content_dir)
        self.template_dir = Path(template_dir)
        self.output_dir = Path(output_dir)
        
        # Initialize Jinja2 environment
        self.jinja_env = Environment(
            loader=FileSystemLoader(str(self.template_dir)),
            autoescape=True
        )
        
        # Initialize markdown processor
        self.md_processor = MarkdownProcessor()
    
    def clean_output(self):
        """Remove all files from output directory."""
        if self.output_dir.exists():
            shutil.rmtree(self.output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
    
    def process_post(self, post_file: Path) -> Post:
        """Process a single post file.
        
        Args:
            post_file: Path to the markdown post file
            
        Returns:
            Processed Post object
        """
        print(f"Processing: {post_file.name}")
        
        # Parse the post
        post = Post(post_file)
        
        # Convert markdown to HTML
        post.html_content = self.md_processor.process(post.content)
        
        return post
    
    def render_post(self, post: Post) -> str:
        """Render a post using Jinja2 template.
        
        Args:
            post: Post object to render
            
        Returns:
            Rendered HTML string
        """
        template = self.jinja_env.get_template('post.html')
        return template.render(post=post.to_dict())
    
    def save_post(self, post: Post, html: str):
        """Save rendered HTML to output directory.
        
        Args:
            post: Post object
            html: Rendered HTML string
        """
        # Create output filename: slug.html
        output_file = self.output_dir / f"{post.slug}.html"
        
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(html)
        
        print(f"Generated: {output_file}")
    
    def generate_post(self, post_file: Path):
        """Process and generate HTML for a single post.
        
        Args:
            post_file: Path to the markdown post file
        """
        post = self.process_post(post_file)
        html = self.render_post(post)
        self.save_post(post, html)
    
    def generate_all(self):
        """Generate HTML for all posts in content directory."""
        print("Starting site generation...")
        print(f"Content directory: {self.content_dir.absolute()}")
        print(f"Output directory: {self.output_dir.absolute()}")
        print()
        
        # Clean output directory
        self.clean_output()
        
        # Find all markdown files
        post_files = list(self.content_dir.glob('**/*.md'))
        
        if not post_files:
            print("No markdown files found in content directory.")
            return
        
        print(f"Found {len(post_files)} post(s)")
        print()
        
        # Process each post
        for post_file in post_files:
            try:
                self.generate_post(post_file)
            except Exception as e:
                print(f"Error processing {post_file.name}: {e}")
        
        print()
        print(f"Site generation complete! {len(post_files)} post(s) generated.")


def main():
    """Main entry point for the generator."""
    import sys
    
    generator = SiteGenerator()
    
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
