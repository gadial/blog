{%- for post in site.posts -%}
{% if post.social_media_share == true %}
{{ post.title}}
{{ post.url}}
{{ post.description}}
**********
{% endif %}
{% endfor %}