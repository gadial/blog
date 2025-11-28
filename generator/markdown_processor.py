"""Markdown processor with math support for Hebrew blog."""
import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
import re


class MathExtension(Extension):
    """Markdown extension for handling LaTeX math expressions."""
    
    def extendMarkdown(self, md):
        """Register the preprocessor."""
        md.preprocessors.register(MathPreprocessor(md), 'math', 175)


class MathPreprocessor(Preprocessor):
    """Preprocessor to protect math expressions from markdown processing."""
    
    def __init__(self, md):
        super().__init__(md)
        self.math_blocks = []
        self.warnings = []
    
    def run(self, lines):
        """Process lines to protect math expressions."""
        text = '\n'.join(lines)
        
        # Protect display math ($$...$$)
        def replace_display_math(match):
            placeholder = f'~~~MATHBLOCK{len(self.math_blocks)}~~~'
            self.math_blocks.append(('display', match.group(1)))
            return placeholder
        
        # Protect inline math ($...$)
        def replace_inline_math(match):
            math_content = match.group(1)
            placeholder = f'~~~MATHBLOCK{len(self.math_blocks)}~~~'
            self.math_blocks.append(('inline', math_content))
            return placeholder
        
        # Process display math first ($$...$$)
        text = re.sub(r'\$\$([^\$]+?)\$\$', replace_display_math, text, flags=re.DOTALL)
        
        # Process inline math ($...$) - allow newlines for multiline expressions like cases
        text = re.sub(r'\$([^\$]+?)\$', replace_inline_math, text, flags=re.DOTALL)
        
        return text.split('\n')


class MarkdownProcessor:
    """Process markdown content with math support."""
    
    def __init__(self):
        """Initialize the markdown processor."""
        self.md = markdown.Markdown(
            extensions=[
                'extra',
                'codehilite',
                'tables',
                'fenced_code',
                'nl2br',
                MathExtension()
            ],
            extension_configs={
                'codehilite': {
                    'css_class': 'highlight',
                    'linenums': False
                }
            }
        )
        self.warnings = []
    
    def process(self, content: str) -> str:
        """Convert markdown to HTML with math support.
        
        Args:
            content: Markdown content string
            
        Returns:
            HTML string with math expressions wrapped for MathJax/KaTeX
        """
        # Reset the markdown processor
        self.md.reset()
        
        # Convert markdown to HTML
        html = self.md.convert(content)
        
        # Restore math blocks and collect warnings
        if hasattr(self.md.preprocessors['math'], 'math_blocks'):
            math_blocks = self.md.preprocessors['math'].math_blocks
            preprocessor_warnings = self.md.preprocessors['math'].warnings
            
            # Collect warnings
            if preprocessor_warnings:
                self.warnings.extend(preprocessor_warnings)
                preprocessor_warnings.clear()
            
            for i, (math_type, math_content) in enumerate(math_blocks):
                placeholder = f'~~~MATHBLOCK{i}~~~'
                # Escape HTML entities in math content to prevent browser parsing issues
                # Replace & with &amp;, < with &lt;, > with &gt;
                escaped_content = (math_content
                                   .replace('&', '&amp;')
                                   .replace('<', '&lt;')
                                   .replace('>', '&gt;'))
                if math_type == 'display':
                    # Wrap display math for rendering
                    replacement = f'<div class="math">\\[{escaped_content}\\]</div>'
                else:  # inline
                    # Wrap inline math for rendering
                    replacement = f'<span class="math">\\({escaped_content}\\)</span>'
                html = html.replace(placeholder, replacement)
            # Clear for next use
            math_blocks.clear()
        
        return html
    
    def get_warnings(self):
        """Get and clear accumulated warnings."""
        warnings = self.warnings.copy()
        self.warnings.clear()
        return warnings
