---
layout: home
---

<div class="hero-section">
  <div class="hero-content">
    <h1>Willkommen bei the more the betta!</h1>
    <p class="hero-subtitle">Entdecke mit mir die faszinierende Welt der Kampffischzucht - von der ersten Paarung bis zum Verkauf</p>
   </div>
  <!-- Großes Hintergrund-Icon -->
  <img src="{{ '/assets/images/misc/icon.webp' | relative_url }}" alt="Betta Background" class="hero-background-icon">
</div>

<!-- Statistiken Card -->
<div class="content-card stats-card">
  <h2>Aktuelle Statistiken</h2>
  <div class="hero-stats">
    <a href="/blog/" class="hero-stat" style="text-decoration:none; color:inherit;">
      <span class="stat-number">{{ site.posts | size }}</span>
      <span class="stat-label">Blog-Einträge</span>
    </a>
    <a href="/fish/" class="hero-stat" style="text-decoration:none; color:inherit;">
      {% assign fish_posts = site.posts | where_exp: "post", "post.categories contains 'fish'" %}
      <span class="stat-number">{{ fish_posts | size }}</span>
      <span class="stat-label">Fisch-Profile</span>
    </a>
    <a href="/tanks/" class="hero-stat" style="text-decoration:none; color:inherit;">
      {% assign tank_posts = site.posts | where_exp: "post", "post.categories contains 'tank'" %}
      {% assign active_tanks = tank_posts | where_exp: "post", "post.aktiv != false" %}
      <span class="stat-number">{{ active_tanks | size }}</span>
      <span class="stat-label">Aktive Becken</span>
    </a>
    {% assign breeding_posts = site.posts | where_exp: "post", "post.categories contains 'breeding' or post.tags contains 'zucht'" %}

      <a href="/tags/zucht/" class="hero-stat" style="text-decoration:none; color:inherit;">
        <div class="stat-number">{{ breeding_posts | size }}</div>
        <div class="stat-label">Zucht-Einträge</div>
      </a>
      <a href="/tags/laichbecken/" class="hero-stat" style="text-decoration:none; color:inherit;">
        <div class="stat-number">0</div>
        <div class="stat-label">Aktive Laichungen</div>
      </a>
      <a href="/tags/jungfische/" class="hero-stat" style="text-decoration:none; color:inherit;">
        <div class="stat-number">~60</div>
        <div class="stat-label">Jungfische im Paradies-Becken</div>
      </a>
  </div>
</div>

<!-- Einleitungstext Card -->
<div class="content-card intro-card">
  <h2>Mein Weg zur Betta-Zucht</h2>
  <p>Hallo und herzlich willkommen! Ich bin Softwareentwicklerin und teste hier zum ersten Mal die Möglichkeiten von Jekyll. Doch dieser Blog dreht sich nicht um Code, sondern um ein ganz anderes Hobby: meine Leidenschaft für die Zucht von Betta-Fischen.</p>
  
  <p>Alles begann mit einem gebrauchten Aquarium, das ich über Kleinanzeigen gefunden habe. Kurz darauf bekam ich zwei weitere Becken geschenkt. Doch schnell wurde klar, dass ich mehr Platz brauche: Ein Quarantänebecken war notwendig, und schließlich auch ein weiteres Aquarium für ein unerwartetes Männchen. Mit der Zeit wuchs mein Interesse an der Zucht, und mittlerweile habe ich bereits erfolgreich Betta-Babys großgezogen! Die Jungfische aus den ersten Zuchten leben jetzt in meinem 160L Paradies-Becken und entwickeln sich prächtig.</p>
  
  <p>In diesem Blog dokumentiere ich die Entwicklung meiner Aquarien, meine Erfahrungen in der Fischzucht und die kleinen und großen Herausforderungen, die dieses Hobby mit sich bringt. Vielleicht findest du hier Inspiration oder hilfreiche Tipps für dein eigenes Aquaristik-Projekt.</p>
</div>

<!-- Call-to-Action Card -->
<div class="content-card cta-card">
  <h2>Möchtest du mehr erfahren?</h2>
  <p>Folge meiner Reise durch die Welt der Betta-Zucht und lerne von meinen Erfahrungen!</p>
  <div class="cta-buttons">
    <a href="{{ '/blog/' | relative_url }}" class="cta-btn primary">Blog durchstöbern</a>
    <a href="{{ '/fish/' | relative_url }}" class="cta-btn primary">Meine Fische</a>
    <a href="{{ '/tanks/' | relative_url }}" class="cta-btn primary">Aquarien</a>
    <a href="{{ '/sale/' | relative_url }}" class="cta-btn primary">Fische kaufen</a>
  </div>
</div>
