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

  <div class="tk-switch">
    <span class="tk-switch-label tk-switch-label-active">Nur aktive Aquarien</span>
    <label class="tk-switch-toggle">
      <input type="checkbox" id="tank-toggle" />
      <span class="tk-switch-slider" aria-hidden="true"></span>
    </label>
    <span class="tk-switch-label tk-switch-label-all">Alle Aquarien</span>
  </div>

  <div class="blog-posts-list tk-list">
    {% assign tank_posts = site.posts | where_exp: "post", "post.categories contains 'tank'" | sort: 'date' | reverse %}
    {% for post in tank_posts %}
    <article class="post-card content-card {% if post.aktiv == false %}tank-inactive{% endif %}" data-tank-status="{% if post.aktiv == false %}inactive{% else %}active{% endif %}">
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

<script>
  (function () {
    const toggle = document.getElementById("tank-toggle");
    const list = document.querySelector(".tk-list");
    const cards = Array.prototype.slice.call(document.querySelectorAll(".tk-list .post-card"));
    if (!toggle || !list || !cards.length) return;

    const STORAGE_KEY = "tankOverviewShowAll";

    function applyFilter(showAll) {
      list.classList.toggle("tk-mode-all", showAll);
    }

    let showAll = false;
    try {
      showAll = window.localStorage.getItem(STORAGE_KEY) === "1";
    } catch (e) {
      showAll = false;
    }
    toggle.checked = showAll;
    applyFilter(showAll);

    toggle.addEventListener("change", function () {
      applyFilter(this.checked);
      try {
        window.localStorage.setItem(STORAGE_KEY, this.checked ? "1" : "0");
      } catch (e) {
        /* ignore storage errors (e.g. private mode) */
      }
    });
  })();
</script>

<style>
  /* Default: nur aktive Aquarien anzeigen (funktioniert auch ohne JavaScript) */
  .tk-list:not(.tk-mode-all) .post-card[data-tank-status="inactive"] {
    display: none;
  }

  .tk-switch {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.7rem;
    margin: 0 auto 1.5rem;
    max-width: 1000px;
  }
  .tk-switch-label {
    font-size: 0.85rem;
    font-weight: 700;
    color: #fff;
    opacity: 0.7;
    transition: opacity 0.2s ease;
  }
  .tk-switch-label-active {
    opacity: 1;
  }
  .tk-switch:has(#tank-toggle:checked) .tk-switch-label-active {
    opacity: 0.55;
  }
  .tk-switch:has(#tank-toggle:checked) .tk-switch-label-all {
    opacity: 1;
  }
  .tk-switch-toggle {
    position: relative;
    display: inline-block;
    width: 46px;
    height: 26px;
    flex-shrink: 0;
  }
  .tk-switch-toggle input {
    opacity: 0;
    width: 0;
    height: 0;
  }
  .tk-switch-slider {
    position: absolute;
    cursor: pointer;
    inset: 0;
    background: rgba(127, 83, 172, 0.25);
    border-radius: 999px;
    transition: background 0.25s ease;
  }
  .tk-switch-slider::before {
    content: "";
    position: absolute;
    width: 20px;
    height: 20px;
    left: 3px;
    top: 3px;
    background: #fff;
    border-radius: 50%;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.25);
    transition: transform 0.25s ease;
  }
  .tk-switch-toggle input:checked + .tk-switch-slider {
    background: linear-gradient(135deg, var(--theme-primary-1, #2ec4b6), var(--theme-primary-3, #7f53ac));
  }
  .tk-switch-toggle input:checked + .tk-switch-slider::before {
    transform: translateX(20px);
  }
  .tk-switch-toggle input:focus-visible + .tk-switch-slider {
    outline: 2px solid var(--theme-primary-1, #2ec4b6);
    outline-offset: 2px;
  }
</style>
