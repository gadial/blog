---
layout: default
---
<h1>פוסטים אקראיים</h1>
<script src="/assets/js/underscore-min.js"></script>
<script src="//cdnjs.cloudflare.com/ajax/libs/list.js/1.5.0/list.min.js"></script>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>


<button id="reroll">להגריל מחדש</button>
<div id="post-list">
  <ul class="list" id="post-list">
  {%- assign date_format = site.minima.date_format | default: "%b %-d, %Y" -%}
  {%- for post in site.posts -%}
    <li>
    <a class="post-link" href="{{ post.url | relative_url }}">
    <h3 class="name">{{ post.title }}</h3>
    </a>
       <p class="date post-meta timestamp" data-timestamp="{{post.date | date_to_xmlschema}}">{{ post.date | date: date_format }}</p>
       <span>
       {% for category in post.categories %}
       <a href="{{site.baseurl}}{{category.url}}">{{category.name}}</a>{% if forloop.last == false %}, {% endif %}
       {% endfor %}
       </span>
       <div hidden class="category">{% for category in post.categories %}{{category.name}}{% if forloop.last == false %}, {% endif %}{% endfor %}</div>
    </li>
  {% endfor %}
  </ul>
</div>

<script type="text/javascript">
$(document).ready(function(){
var options = {
  valueNames: [ 'name', 'date', { name: 'timestamp', attr: 'data-timestamp' }, 'category']
};
var postList = new List('post-list', options);
var choose_random = function(n){
  elements = _.sample(postList.items, n)
  postList.filter(function(item) {
    for (var i = 0; i < n; i++){
      if (elements[i].values().name == item.values().name){
        return true;
      }
    }
    return false;
  });
}

choose_random(5);

$('#reroll').click(function() {
  choose_random(5);
});

});
</script>
