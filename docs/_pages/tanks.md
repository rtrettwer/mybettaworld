---
layout: default
title: "Aquarien"
permalink: /tanks/
---

<div class="blog-container">
  <div class="blog-header-card content-card">
    <h1>Aquarien</h1>
    <p>Hier findest du eine Übersicht über all meine Aquarien - von der Zucht bis zur Quarantäne</p>
  </div>

  <div class="blog-posts-list">
    {% assign tank_posts = site.posts | where_exp: "post", "post.categories contains 'tank'" | sort: 'date' | reverse %}
    {% for post in tank_posts %}
    <article class="post-card content-card {% if post.aktiv == false %}tank-inactive{% endif %}">
      <div class="post-header">
        <span class="post-meta">
          {% if post.dimensions %}{{ post.dimensions }}{% endif %}
          {% if post.fassungsvermoegen %} • {{ post.fassungsvermoegen }}{% endif %}
          {% if post.aktiv == false %} • <span style="color: #999; font-weight: bold;">⚠️ Inaktiv seit {{ post.inaktiv_seit }}</span>{% endif %}
        </span>
        <h2>
          <a class="post-link" href="{{ post.url | relative_url }}">
            {{ post.title | escape }}
          </a>
        </h2>
      </div>

      {% if post.image %}
      <div class="post-image" style="margin-bottom: 1rem;">
        <img src="{{ post.image | relative_url }}" alt="{{ post.title }}" style="width: 100%; height: 200px; object-fit: cover; border-radius: 8px; {% if post.aktiv == false %}filter: grayscale(100%); opacity: 0.7;{% endif %}">
      </div>
      {% endif %}

      <div class="post-excerpt">
        {{ post.excerpt }}
        {% if post.water_type or post.filter or post.beleuchtung %}
        <div class="tank-info-box" style="margin-top: 1rem; padding: 1rem; border-radius: 12px; font-size: 0.9rem; border: 2px solid transparent; background: linear-gradient(rgba(248,249,250,0.95), rgba(248,249,250,0.95)) padding-box, linear-gradient(135deg, var(--theme-primary-1), var(--theme-primary-2), var(--theme-primary-3)) border-box; box-shadow: 0 2px 8px rgba(46, 196, 182, 0.1); transition: all 0.3s ease;">
          {% if post.water_type %}<strong>💧 Wasserart:</strong> {{ post.water_type }}<br>{% endif %}
          {% if post.filter %}<strong>🔄 Filter:</strong> {{ post.filter }}<br>{% endif %}
          {% if post.beleuchtung %}<strong>💡 Beleuchtung:</strong> {{ post.beleuchtung }}{% endif %}
        </div>
        {% endif %}
      </div>

      <div class="post-footer">
        <a class="read-more-btn" href="{{ post.url | relative_url }}">Details ansehen</a>

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
</div>
