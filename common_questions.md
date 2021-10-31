---
layout: default
---
<h1>תשובות לשאלות נפוצות</h1>

בדף הזה אני מרכז שאילתות חיפוש נפוצות שמובילות אל האתר, והפוסט המתאים ביותר לענות עליהן.

<div class="row">
  {% for post in site.data.search_quries %}
  <figure class="col-md-4">
  <h3><a href="{{site.baseurl}}{{post.url}}">{{ post.title }}</a></h3>
  <p>{{post.query}}</p>
  </figure>
  {% endfor %}
</div>