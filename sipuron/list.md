---
layout: clear
title: סיפורונובמבר - הסיפורים
---

<script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

<div id="sipuron-list">
  <button class="sort" data-sort="name">מיון על פי שם</button>
  <button class="sort" data-sort="timestamp">מיון על פי תאריך</button>
  <ul class="list" id="post-list">
  {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
  {%- for sipuron in site.data.sipuron -%}
    <li>
    <h3 class="author">{{ sipuron.author }}</h3>
    <h4 class="keyword">{{ sipuron.keyword }}</h4>
    <p style="white-space: pre-line;">{{ sipuron.story }}</p>
    </li>
  {% endfor %}
  </ul>
</div>