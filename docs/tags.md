---
layout: default
title: Tags
permalink: /tags/
---

<h1>Tags</h1>
<ul>
  {% assign tags_list = site.tags | sort %}
  {% for tag in tags_list %}
    <li>
      <a href="/tags/{{ tag[0] | slugify }}/">{{ tag[0] }}</a> ({{ tag[1].size }})
    </li>
  {% endfor %}
</ul>

