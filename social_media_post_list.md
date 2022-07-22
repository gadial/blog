---
---
[
  {% for post in site.posts %}
  {% if post.social_media_share == true %}
    {
      "date": "{{ post.date }}",
      "title": "{{ post.title }}",
      "description": "{{ post.description}}",
      "url": "{{ post.url }}"
    },
    {% endif %}
  {% endfor %}
]