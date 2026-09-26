"""Jekyll compatibility layer for processing Jekyll-specific syntax."""
import html
import re


class JekyllProcessor:
    """Process Jekyll-specific tags and convert them to standard formats."""
    
    def __init__(self, site_config=None):
        """Initialize Jekyll processor.
        
        Args:
            site_config: Dictionary with site configuration (baseurl, post_images, etc.)
        """
        self.site_config = site_config or {}
        self.baseurl = self.site_config.get('baseurl', '')
        self.post_images = self.site_config.get('post_images', '/images/posts')
    
    def process_equation_tags(self, content: str) -> str:
        """Convert Jekyll {% equation %}...{% endequation %} to LaTeX $...$.
        
        Args:
            content: Markdown content with Jekyll equation tags
            
        Returns:
            Content with equation tags converted to LaTeX delimiters
        """
        # Replace equation tags with inline math $...$
        # Jekyll {% equation %} is typically used for inline equations
        content = re.sub(
            r'{%\s*equation\s*%}(.*?){%\s*endequation\s*%}',
            r'$\1$',
            content,
            flags=re.DOTALL
        )
        
        # Handle inline equation tags if they exist (e.g., {% eq %}...{% endeq %})
        content = re.sub(
            r'{%\s*eq\s*%}(.*?){%\s*endeq\s*%}',
            r'$\1$',
            content,
            flags=re.DOTALL
        )
        
        return content
    
    def process_site_variables(self, content: str) -> str:
        """Replace Jekyll site variables with configured values.
        
        Handles patterns like:
        - {{site.baseurl}}{{site.post_images}}
        - {{site.baseurl}}/path/to/file
        - {{ site.post_images }}
        
        Args:
            content: Content with Jekyll variables
            
        Returns:
            Content with variables replaced
        """
        # Replace {{site.baseurl}}{{site.post_images}} with the combined path
        combined_pattern = r'{{\s*site\.baseurl\s*}}{{\s*site\.post_images\s*}}'
        content = re.sub(combined_pattern, self.baseurl + self.post_images, content)
        
        # Replace individual {{site.post_images}}
        content = re.sub(r'{{\s*site\.post_images\s*}}', self.post_images, content)
        
        # Replace {{site.baseurl}}
        content = re.sub(r'{{\s*site\.baseurl\s*}}', self.baseurl, content)
        
        return content
    
    def process_liquid_tags(self, content: str) -> str:
        """Remove or convert other Liquid template tags.
        
        Args:
            content: Content with Liquid tags
            
        Returns:
            Content with tags processed
        """
        # Raw highlights look like code blocks, but contain prose rather than code.
        # Emit their HTML directly so Markdown/Pygments does not syntax-highlight it.
        def replace_raw_highlight(match):
            raw_text = match.group(1).strip('\r\n')
            escaped_text = html.escape(raw_text)
            escaped_text = re.sub(r'\r\n?|\n', '<br>\n', escaped_text)
            return (
                '<div class="highlight raw-highlight">'
                f'{escaped_text}'
                '</div>'
            )

        content = re.sub(
            r'{%\s*highlight\s+raw\s*%}(.*?){%\s*endhighlight\s*%}',
            replace_raw_highlight,
            content,
            flags=re.DOTALL | re.IGNORECASE
        )

        # Convert language-specific highlights to Markdown fenced code blocks.
        content = re.sub(r'{%\s*highlight\s+(\w+)\s*%}', r'```\1', content)
        content = re.sub(r'{%\s*endhighlight\s*%}', '```', content)
        
        return content
    
    def process(self, content: str) -> str:
        """Process all Jekyll-specific syntax in content.
        
        Args:
            content: Raw markdown content from Jekyll
            
        Returns:
            Processed content with Jekyll syntax converted
        """
        # Process in order
        content = self.process_equation_tags(content)
        content = self.process_site_variables(content)
        content = self.process_liquid_tags(content)
        
        return content
