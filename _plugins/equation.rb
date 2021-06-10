module Jekyll
    class EquationTag < Liquid::Block
  
      def initialize(tag_name, text, tokens)
          super
          @text = text
      end
  
      def render(context)
        text = super
        "<span>\\( #{text} \\)</span>"
      end
    end
  end
  
  Liquid::Template.register_tag('equation', Jekyll::EquationTag)