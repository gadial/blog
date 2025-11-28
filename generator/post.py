"""Post parser module for static site generator."""
import frontmatter
from pathlib import Path
from typing import Dict, Any
from datetime import datetime


class Post:
    """Represents a blog post with frontmatter and content."""
    
    def __init__(self, filepath: Path):
        """Initialize post from a markdown file.
        
        Args:
            filepath: Path to the markdown file
        """
        self.filepath = filepath
        self.metadata: Dict[str, Any] = {}
        self.content: str = ""
        self.html_content: str = ""
        self._parse()
    
    def _parse(self):
        """Parse the markdown file and extract frontmatter."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            post = frontmatter.load(f)
            self.metadata = dict(post.metadata)
            self.content = post.content
    
    @property
    def title(self) -> str:
        """Get post title from metadata."""
        return self.metadata.get('title', 'Untitled')
    
    @property
    def date(self) -> datetime:
        """Get post date from metadata or filename."""
        date_val = self.metadata.get('date')
        if isinstance(date_val, datetime):
            return date_val
        elif isinstance(date_val, str):
            # Try to parse common date formats
            for fmt in ['%Y-%m-%d', '%Y-%m-%d %H:%M:%S', '%Y/%m/%d']:
                try:
                    return datetime.strptime(date_val, fmt)
                except ValueError:
                    continue
        
        # Try to extract date from filename (Jekyll format: YYYY-MM-DD-title.md)
        import re
        filename = self.filepath.stem
        date_match = re.match(r'^(\d{4})-(\d{2})-(\d{2})-', filename)
        if date_match:
            year, month, day = date_match.groups()
            return datetime(int(year), int(month), int(day))
        
        return datetime.now()
    
    @property
    def layout(self) -> str:
        """Get post layout from metadata."""
        return self.metadata.get('layout', 'post')
    
    @property
    def categories(self) -> list:
        """Get post categories from metadata."""
        cats = self.metadata.get('categories', [])
        if isinstance(cats, str):
            return [cats]
        return cats if isinstance(cats, list) else []
    
    @property
    def tags(self) -> list:
        """Get post tags from metadata."""
        tags = self.metadata.get('tags', [])
        if isinstance(tags, str):
            return [tags]
        return tags if isinstance(tags, list) else []
    
    @property
    def slug(self) -> str:
        """Generate URL slug from filename or title.
        
        Removes YYYY-MM-DD- prefix from Jekyll-style filenames.
        """
        stem = self.filepath.stem
        # Remove date prefix if present (YYYY-MM-DD-)
        import re
        slug = re.sub(r'^\d{4}-\d{2}-\d{2}-', '', stem)
        return slug if slug else stem
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert post to dictionary for template rendering."""
        return {
            'title': self.title,
            'date': self.date,
            'content': self.html_content,
            'layout': self.layout,
            'categories': self.categories,
            'tags': self.tags,
            'slug': self.slug,
            'metadata': self.metadata
        }
