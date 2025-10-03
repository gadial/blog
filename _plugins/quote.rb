# _plugins/quote_tag.rb
module Jekyll
  class QuoteTag < Liquid::Block

    def initialize(tag_name, text, tokens)
      super
      @direction = parse_direction(text)
    end

    def render(context)
      body = super          # body is already rendered by inner converters
      <<~HTML
        <blockquote dir="#{@direction}" class="quote-#{@direction}">
        #{body.strip}
        </blockquote>
      HTML
    end

    private

    # Map the user’s parameter to a safe dir value.
    def parse_direction(text)
      dir = text.to_s.strip.downcase
      case dir
      when 'rtl', 'he', 'heb', 'hebrew' then 'rtl'
      when 'ltr', 'en', 'eng', 'english' then 'ltr'
      else 'ltr'                         # graceful fallback
      end
    end
  end
end

Liquid::Template.register_tag('quote', Jekyll::QuoteTag)
