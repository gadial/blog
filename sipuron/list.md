---
layout: clear
title: סיפורונובמבר - הסיפורים
---

<script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>

<div id="sipuron-list">
<label>חיפוש בטקסט הסיפורים</label>
<input class="search" id="story-search"/>
<button class="sort" data-sort="author">מיון על פי שם מזהה</button>
<button class="sort" data-sort="keyword">מיון על פי מילת מפתח</button>
<button class="sort" data-sort="length">מיון על פי אורך</button>
  <ul class="list" >
  {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
  {%- for sipuron in site.data.sipuron -%}
    <li>
    <h3 class="author">{{ sipuron.author }}</h3>
    <h4 class="keyword">{{ sipuron.keyword }}</h4>
    <p class="story" style="white-space: pre-line;">{{ sipuron.story }}</p>
    <div hidden class="length">{{ sipuron.length }}</div>
    </li>
  {% endfor %}
  </ul>
</div>

<script type="text/javascript">
$(document).ready(function(){
var options = {
  valueNames: [ 'author', 'keyword', 'length', 'story'],
  searchColumns: ['story']
};
var postList = new List('sipuron-list', options);
});
</script>