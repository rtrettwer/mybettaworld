---
layout: default
title: "Futter"
permalink: /food/
---

<div class="blog-container">
  <div class="blog-header-card content-card">
    <h1>Futter</h1>
    <p>Alles über die Ernährung meiner Kampffische - von Lebendfutter bis zur täglichen Routine</p>
  </div>

  <div class="blog-posts-list">
    {% assign food_posts = site.posts | where_exp: "post", "post.categories contains 'food'" | sort: 'date' | reverse %}
    {% for post in food_posts %}
    <article class="post-card content-card">
      <div class="post-header">
        <span class="post-meta">
          {% if post.tags and post.tags.size > 0 %}
            {% for tag in post.tags limit: 3 %}
              <span class="food-tag">{{ tag }}</span>{% unless forloop.last %} • {% endunless %}
            {% endfor %}
          {% endif %}
        </span>
        <h2>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
        </h2>
      </div>

      {% if post.image %}
      <div class="post-image" style="margin-bottom: 1rem;">
        <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px;">
      </div>
      {% endif %}

      <div class="post-excerpt">
        {{ post.excerpt }}
        {% if post.categories contains 'food' %}
        <div style="margin-top: 1rem; padding: 1rem; background: linear-gradient(135deg, rgba(46, 196, 182, 0.05), rgba(127, 83, 172, 0.05)); border-radius: 8px; font-size: 0.9rem; border-left: 3px solid var(--theme-primary-3);">
          <strong>🍽️ Futterart:</strong> 
          {% if post.tags contains 'lebendfutter' %}
            <span style="color: var(--theme-primary-1); font-weight: 600;">Lebendfutter</span>
          {% elsif post.tags contains 'routine' %}
            <span style="color: var(--theme-primary-2); font-weight: 600;">Fütterungsroutine</span>
          {% elsif post.tags contains 'granulat' %}
            <span style="color: var(--theme-primary-3); font-weight: 600;">Trockenfutter</span>
          {% else %}
            <span style="color: var(--theme-primary-1); font-weight: 600;">Spezialfutter</span>
          {% endif %}
        </div>
        {% endif %}
      </div>

      <div class="post-footer">
        <a class="read-more-btn" href="{{ post.url | relative_url }}">Futter-Guide lesen</a>

        {%- if post.tags and post.tags.size > 0 -%}
          <div class="post-tags">
            <strong>Tags: </strong>
            {%- for tag in post.tags -%}
              <a class="tag-link" href="/tags/{{ tag | slugify }}/">{{ tag }}</a>
            {%- endfor -%}
          </div>
        {%- endif -%}
      </div>
    </article>
    {% endfor %}
  </div>

  <!-- Zusätzliche Info-Karte für Futter-Tipps -->
  <div class="content-card" style="margin-top: 3rem; background: linear-gradient(135deg, rgba(46, 196, 182, 0.03), rgba(127, 83, 172, 0.03));">
    <h2 style="color: var(--theme-primary-2); margin-bottom: 1rem;">💡 Fütterungs-Tipps</h2>
    <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 1.5rem;">
      <div style="padding: 1rem; background: var(--theme-white); border-radius: 8px; border-left: 3px solid var(--theme-primary-1);">
        <h4 style="color: var(--theme-primary-1); margin-bottom: 0.5rem;">🔄 Abwechslung</h4>
        <p style="margin: 0; font-size: 0.9rem;">Verschiedene Futtersorten sorgen für eine ausgewogene Ernährung und mehr Farbenpracht.</p>
      </div>
      <div style="padding: 1rem; background: var(--theme-white); border-radius: 8px; border-left: 3px solid var(--theme-primary-2);">
        <h4 style="color: var(--theme-primary-2); margin-bottom: 0.5rem;">⏰ Regelmäßigkeit</h4>
        <p style="margin: 0; font-size: 0.9rem;">Feste Fütterungszeiten helfen bei der Gesundheit und dem Wohlbefinden der Fische.</p>
      </div>
      <div style="padding: 1rem; background: var(--theme-white); border-radius: 8px; border-left: 3px solid var(--theme-primary-3);">
        <h4 style="color: var(--theme-primary-3); margin-bottom: 0.5rem;">🎯 Portionsgröße</h4>
        <p style="margin: 0; font-size: 0.9rem;">Lieber weniger und öfter füttern - Bettas haben kleine Mägen.</p>
      </div>
    </div>
  </div>
</div>
