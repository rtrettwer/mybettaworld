---
layout: home
---

<div class="hero-section">
  <div class="hero-content">
    <h1>Willkommen in meiner Betta-Welt!</h1>
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
      <span class="stat-number">6</span>
      <span class="stat-label">Becken</span>
    </a>
  </div>
</div>

<!-- Einleitungstext Card -->
<div class="content-card intro-card">
  <h2>Mein Weg zur Betta-Zucht</h2>
  <p>Hallo und herzlich willkommen! Ich bin Softwareentwicklerin und teste hier zum ersten Mal die Möglichkeiten von Jekyll. Doch dieser Blog dreht sich nicht um Code, sondern um ein ganz anderes Hobby: meine Leidenschaft für die Zucht von Betta-Fischen.</p>
  
  <p>Alles begann mit einem gebrauchten Aquarium, das ich über Kleinanzeigen gefunden habe. Kurz darauf bekam ich zwei weitere Becken geschenkt. Doch schnell wurde klar, dass ich mehr Platz brauche: Ein Quarantänebecken war notwendig, und schließlich auch ein weiteres Aquarium für ein unerwartetes Männchen. Mit der Zeit wuchs mein Interesse an der Zucht, und heute kümmere ich mich um drei Laichungen voller Betta-Babys, die ich großziehen und später verkaufen möchte.</p>
  
  <p>In diesem Blog dokumentiere ich die Entwicklung meiner Aquarien, meine Erfahrungen in der Fischzucht und die kleinen und großen Herausforderungen, die dieses Hobby mit sich bringt. Vielleicht findest du hier Inspiration oder hilfreiche Tipps für dein eigenes Aquaristik-Projekt.</p>
</div>

<!-- Zucht-Fortschritt Card -->
<div class="content-card breeding-card">
  {% include breeding_tracker.html %}
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
