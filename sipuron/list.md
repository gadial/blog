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
<br />
<label for="authors">סינון על פי שם מזהה</label>
<select name="authors" id="authors_filter" multiple>
<option value="הכל">הכל</option>
{%- for author in site.data.sipuron.authors -%}
<option value="{{author}}">{{author}}</option>
{% endfor %}
</select>

<label for="keywords">סינון על פי מילת מפתח</label>
<select name="keywords" id="keywords_filter" multiple>
<option value="הכל">הכל</option>
{%- for keyword in site.data.sipuron.keywords -%}
<option value="{{keyword}}">{{keyword}}</option>
{% endfor %}
</select>


  <ul class="list" >
  {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
  {%- for sipuron in site.data.sipuron.stories -%}
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

function passes_filters(item){
  var selected_authors = $('#authors_filter').val();
  var selected_keywords = $('#keywords_filter').val();
   if ((selected_authors.includes("הכל") || selected_authors.length == 0 || selected_authors.includes(item.values().author)) &&
      (selected_keywords.includes("הכל") || selected_keywords.length == 0 || selected_keywords.includes(item.values().keyword))){
        return true;
      } else {
        return false;
      }
    return false;
}

$('#authors_filter').change(function() {
    postList.filter(passes_filters);        
});

$('#keywords_filter').change(function() {
    postList.filter(passes_filters);
});

});
</script>