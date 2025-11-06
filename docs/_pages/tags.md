---
layout: page
title: Tags
permalink: /tags/
---

<!-- Card-Container für saubere Darstellung -->
<div class="cards-container">
  <div class="content-card">
    <h2>Alle Tags</h2>
    <p>Hier findest du alle verwendeten Tags und kannst nach spezifischen Themen suchen.</p>
    
    <div class="tags-grid">
      {% assign tags_list = site.tags | sort %}
      {% for tag in tags_list %}
        <div class="tag-card">
          <a href="/tags/{{ tag[0] | slugify }}/" class="tag-link">
            <h3>{{ tag[0] }}</h3>
            <span class="tag-count">{{ tag[1].size }} {% if tag[1].size == 1 %}Beitrag{% else %}Beiträge{% endif %}</span>
          </a>
        </div>
      {% endfor %}
    </div>
  </div>
</div>
