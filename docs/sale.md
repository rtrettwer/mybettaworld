---
layout: default
title: "Verkauf"
permalink: /sale/
---

<div class="blog-header-card content-card">
  <h1>Verkauf</h1>
  <p>Hier findest du alle aktuell verfügbaren Betta-Fische und weitere Angebote.</p>
</div>

<div class="blog-container">
  <!-- Filter Card -->
  <div class="content-card">
    <div class="sales-gallery">
      <!-- Erweiterte Filter -->
      <div class="advanced-filters" id="advanced-filters" style="display: none;">
        <div class="filter-row">
          <label for="search-fish">Suche:</label>
          <input type="search" id="search-fish" placeholder="Name, Farbe oder Beschreibung...">
        </div>
        <div class="filter-row">
          <label for="status-filter">Status:</label>
          <select id="status-filter" data-status-filter>
            <option value="all">Alle Status</option>
            <option value="available">Verfügbar</option>
            <option value="reserved">Reserviert</option>
            <option value="sold">Verkauft</option>
          </select>
        </div>
        <div class="filter-row">
          <label for="price-range">Max. Preis:</label>
          <input type="range" id="price-range" min="0" max="200" value="200" step="10">
          <span id="price-display">200€</span>
        </div>
        <button class="filter-toggle" onclick="resetAllFilters()">Alle Filter zurücksetzen</button>
      </div>

      <!-- Standard Filter Controls -->
      <div class="filter-controls">
        <button class="filter-btn active" data-filter="all">Alle anzeigen</button>
        <button class="filter-btn" data-filter="male">Männchen</button>
        <button class="filter-btn" data-filter="female">Weibchen</button>
        <button class="filter-btn" data-filter="juvenile">Jungfische</button>
        <button class="filter-toggle" onclick="toggleAdvancedFilters()">Erweiterte Filter</button>
      </div>

      <!-- Sortier- und Ergebnis-Controls -->
      <div class="sort-controls">
        <div class="results-count">
          <span id="results-count">Lade Fische...</span>
        </div>
        <div class="sort-dropdown">
          <label for="sort-select">Sortieren nach:</label>
          <select id="sort-select">
            <option value="name">Name</option>
            <option value="price-low">Preis (niedrig → hoch)</option>
            <option value="price-high">Preis (hoch → niedrig)</option>
            <option value="status">Verfügbarkeit</option>
          </select>
        </div>
      </div>

      <!-- Keine Ergebnisse Nachricht -->
      <div class="no-results" id="no-results" style="display: none;">
        <div class="no-results-icon">🐠</div>
        <h3>Keine Fische gefunden</h3>
        <p>Versuche es mit anderen Filtereinstellungen oder schaue später wieder vorbei.</p>
        <button class="reset-filters-btn" onclick="showAllFish()">Alle Fische anzeigen</button>
      </div>
    </div>
  </div>

  <!-- Einzelne Fisch-Cards -->
  {% for fish in site.data.sales %}
  <div class="content-card fish-card {{ fish.status }}"
       data-category="{{ fish.gender }}"
       data-price="{{ fish.price | default: 0 }}"
       data-status="{{ fish.status | default: 'sold' }}"
       style="overflow: hidden; position: relative; transition: all 0.4s ease;">
    
    <!-- Fisch Bild Section -->
    <div class="fish-image-section" style="position: relative; height: 280px; overflow: hidden; border-radius: 12px 12px 0 0; margin: -2rem -2rem 0 -2rem;">
      <img src="{{ fish.image | relative_url }}" alt="{{ fish.name }}" loading="lazy"
           onerror="this.src='/assets/images/placeholder-fish.jpg'"
           style="width: 100%; height: 100%; object-fit: cover; transition: all 0.4s ease;">
      
      <!-- Overlay Gradient -->
      <div style="position: absolute; bottom: 0; left: 0; right: 0; height: 60px; background: linear-gradient(to top, rgba(0,0,0,0.6), transparent); pointer-events: none;"></div>
      
      <!-- Price Tag -->
      <div class="price-tag" style="position: absolute; top: 15px; right: 15px; background: linear-gradient(135deg, var(--theme-primary-1), var(--theme-primary-2)); color: white; padding: 0.7rem 1.3rem; border-radius: 25px; font-weight: 700; font-size: 1.2rem; box-shadow: 0 4px 20px rgba(0,0,0,0.3); backdrop-filter: blur(10px);">{{ fish.price }}€</div>
      
      <!-- Status Badge -->
      <div class="status-badge {{ fish.status }}" style="position: absolute; top: 15px; left: 15px; padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.8rem; font-weight: 700; text-transform: uppercase; backdrop-filter: blur(10px); letter-spacing: 0.5px;
        {% if fish.status == 'available' %}background: linear-gradient(135deg, #4caf50, #66bb6a); color: white; box-shadow: 0 3px 15px rgba(76, 175, 80, 0.4);
        {% elsif fish.status == 'reserved' %}background: linear-gradient(135deg, #ff9800, #ffb74d); color: white; box-shadow: 0 3px 15px rgba(255, 152, 0, 0.4);
        {% elsif fish.status == 'sold' %}background: linear-gradient(135deg, #f44336, #ef5350); color: white; box-shadow: 0 3px 15px rgba(244, 67, 54, 0.4);
        {% endif %}">
        {% if fish.status == 'available' %}Verfügbar
        {% elsif fish.status == 'reserved' %}Reserviert
        {% elsif fish.status == 'sold' %}Verkauft
        {% endif %}
      </div>
      
      <!-- Fish Name Overlay -->
      <div style="position: absolute; bottom: 15px; left: 15px; right: 15px;">
        <h2 style="margin: 0; color: white; font-size: 1.8rem; font-weight: 700; text-shadow: 0 2px 8px rgba(0,0,0,0.7);">{{ fish.name }}</h2>
      </div>
    </div>
    
    <!-- Fisch Informationen -->
    <div class="fish-content" style="padding: 1.5rem 0 0 0;">
      <!-- Fish Details Tags -->
      <div class="fish-details" style="display: flex; flex-wrap: wrap; gap: 0.8rem; margin-bottom: 1.5rem;">
        <span class="gender-tag {{ fish.gender }}" style="padding: 0.5rem 1rem; border-radius: 20px; font-size: 0.9rem; font-weight: 600; display: flex; align-items: center; gap: 0.3rem;
          {% if fish.gender == 'male' %}background: linear-gradient(135deg, #2196f3, #42a5f5); color: white; box-shadow: 0 2px 10px rgba(33, 150, 243, 0.3);
          {% elsif fish.gender == 'female' %}background: linear-gradient(135deg, #e91e63, #f06292); color: white; box-shadow: 0 2px 10px rgba(233, 30, 99, 0.3);
          {% else %}background: linear-gradient(135deg, #9c27b0, #ba68c8); color: white; box-shadow: 0 2px 10px rgba(156, 39, 176, 0.3);
          {% endif %}">
          {% if fish.gender == 'male' %}<span>♂</span> Männchen
          {% elsif fish.gender == 'female' %}<span>♀</span> Weibchen
          {% else %}<span>?</span> Unbekannt
          {% endif %}
        </span>
        
        {% if fish.age %}
        <span class="detail-tag" style="background: rgba(46, 196, 182, 0.1); color: var(--theme-primary-2); padding: 0.4rem 0.8rem; border-radius: 15px; font-size: 0.85rem; font-weight: 500; border: 1px solid rgba(46, 196, 182, 0.2);">
          <span style="opacity: 0.7;">🕐</span> {{ fish.age }}
        </span>
        {% endif %}
        
        {% if fish.size %}
        <span class="detail-tag" style="background: rgba(46, 196, 182, 0.1); color: var(--theme-primary-2); padding: 0.4rem 0.8rem; border-radius: 15px; font-size: 0.85rem; font-weight: 500; border: 1px solid rgba(46, 196, 182, 0.2);">
          <span style="opacity: 0.7;">📏</span> {{ fish.size }}
        </span>
        {% endif %}
        
        {% if fish.color %}
        <span class="detail-tag" style="background: rgba(46, 196, 182, 0.1); color: var(--theme-primary-2); padding: 0.4rem 0.8rem; border-radius: 15px; font-size: 0.85rem; font-weight: 500; border: 1px solid rgba(46, 196, 182, 0.2);">
          <span style="opacity: 0.7;">🎨</span> {{ fish.color }}
        </span>
        {% endif %}
      </div>
      
      <!-- Description -->
      {% if fish.description %}
      <div class="description" style="margin-bottom: 1.5rem;">
        <p style="font-size: 1rem; line-height: 1.6; color: #555; margin: 0;">{{ fish.description }}</p>
      </div>
      {% endif %}
      
      <!-- Special Notes -->
      {% if fish.special_notes %}
      <div class="special-notes" style="background: linear-gradient(135deg, rgba(255, 193, 7, 0.08), rgba(255, 152, 0, 0.08)); border: 1px solid rgba(255, 193, 7, 0.2); border-radius: 12px; padding: 1rem; margin-bottom: 1.5rem; position: relative;">
        <div style="position: absolute; left: 12px; top: 12px; width: 4px; height: calc(100% - 24px); background: linear-gradient(to bottom, #ffc107, #ff9800); border-radius: 2px;"></div>
        <div style="padding-left: 1rem;">
          <strong style="color: #f57c00; font-size: 0.9rem;">✨ Besonderheit:</strong>
          <p style="color: #666; margin: 0.3rem 0 0 0; font-size: 0.9rem; line-height: 1.5;">{{ fish.special_notes }}</p>
        </div>
      </div>
      {% endif %}
      
      <!-- Contact Info -->
      <div class="contact-info" style="border-top: 1px solid rgba(46, 196, 182, 0.1); padding-top: 1.5rem; text-align: center;">
        {% if fish.status == 'available' %}
          <button class="interest-btn" style="background: linear-gradient(135deg, var(--theme-primary-1), var(--theme-primary-2)); color: white; border: none; padding: 1rem 2rem; border-radius: 30px; font-weight: 700; cursor: pointer; transition: all 0.3s ease; font-size: 1rem; width: 100%; margin-bottom: 1rem; box-shadow: 0 4px 20px rgba(46, 196, 182, 0.3);" onmouseover="this.style.transform='translateY(-3px)'; this.style.boxShadow='0 8px 30px rgba(46, 196, 182, 0.5)'" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='0 4px 20px rgba(46, 196, 182, 0.3)'">
            <span style="margin-right: 0.5rem;">💌</span> Interesse anmelden
          </button>
          <small style="color: #888; font-style: italic; font-size: 0.85rem;">Nur Abholung möglich • 82008 Unterhaching</small>
        {% elsif fish.status == 'reserved' %}
          <button class="interest-btn" disabled style="background: linear-gradient(135deg, #e0e0e0, #bdbdbd); color: #757575; border: none; padding: 1rem 2rem; border-radius: 30px; font-weight: 700; cursor: not-allowed; font-size: 1rem; width: 100%; margin-bottom: 1rem;">
            <span style="margin-right: 0.5rem;">⏳</span> Reserviert
          </button>
          {% if fish.pickup_date %}
            <small style="color: #888; font-size: 0.85rem;">Abholung: {{ fish.pickup_date | date: "%d.%m.%Y" }}</small>
          {% endif %}
        {% elsif fish.status == 'sold' %}
          <button class="interest-btn" disabled style="background: linear-gradient(135deg, #e0e0e0, #bdbdbd); color: #757575; border: none; padding: 1rem 2rem; border-radius: 30px; font-weight: 700; cursor: not-allowed; font-size: 1rem; width: 100%; margin-bottom: 1rem;">
            <span style="margin-right: 0.5rem;">✓</span> Verkauft
          </button>
          {% if fish.sold_date %}
            <small style="color: #888; font-size: 0.85rem;">Verkauft am {{ fish.sold_date | date: "%d.%m.%Y" }}</small>
          {% endif %}
        {% endif %}
      </div>
    </div>
  </div>
  {% endfor %}

  <!-- Entfernte Spezial-Angebote und Schwimmpflanzen-Kachel, da alles jetzt einheitlich über sales.yml läuft. -->

</div>

<!-- Info-Kachel: Weitere Angebote auf Kleinanzeigen -->
<div class="content-card" style="margin-top: 2.5rem;">
  <h3 style="margin-top: 0;">🔗 Weitere Angebote auf Kleinanzeigen</h3>
  <p>Du findest meine aktuellen Angebote auch auf <a href="https://www.kleinanzeigen.de/s-bestandsliste.html?userId=36951586" target="_blank" rel="noopener" style="font-weight:bold;color:var(--theme-primary-2);text-decoration:underline;">Kleinanzeigen.de</a>.<br>
  Dort gibt es ggf. weitere Fotos und Infos zu den Fischen.</p>
</div>

<!-- JavaScript für Filter-Funktionalität -->
<script src="{{ '/assets/js/sales-filter.js' | relative_url }}"></script>
<script>
// Zusätzliche JavaScript-Funktionen direkt im HTML
function toggleAdvancedFilters() {
  const advancedFilters = document.getElementById('advanced-filters');
  const isVisible = advancedFilters.style.display !== 'none';
  advancedFilters.style.display = isVisible ? 'none' : 'block';

  const toggleBtn = event.target;
  toggleBtn.textContent = isVisible ? '🔧 Erweiterte Filter' : '🔧 Filter ausblenden';
}

function resetAllFilters() {
  // Filter-Buttons zurücksetzen
  document.querySelectorAll('.filter-btn').forEach(btn => btn.classList.remove('active'));
  document.querySelector('[data-filter="all"]').classList.add('active');

  // Eingabefelder zurücksetzen
  document.getElementById('search-fish').value = '';
  document.getElementById('status-filter').value = 'all';
  document.getElementById('price-range').value = '200';
  document.getElementById('price-display').textContent = '200€';
  document.getElementById('sort-select').value = 'name';

  // Alle Fische anzeigen
  showAllFish();
  updateResultsCount();
}

function updateResultsCount() {
  const visibleCards = document.querySelectorAll('.fish-card:not([style*="display: none"])').length;
  const totalCards = document.querySelectorAll('.fish-card').length;
  const resultsCount = document.getElementById('results-count');
  const noResults = document.getElementById('no-results');

  if (visibleCards === 0) {
    resultsCount.textContent = 'Keine Ergebnisse';
    noResults.style.display = 'block';
  } else {
    resultsCount.textContent = `${visibleCards} von ${totalCards} Fischen`;
    noResults.style.display = 'none';
  }
}

// Event Listeners für erweiterte Funktionen
document.addEventListener('DOMContentLoaded', function() {
  // Preis-Range Display Update
  const priceRange = document.getElementById('price-range');
  const priceDisplay = document.getElementById('price-display');

  if (priceRange && priceDisplay) {
    priceRange.addEventListener('input', function() {
      priceDisplay.textContent = this.value + '€';
    });
  }

  // Sortierung
  const sortSelect = document.getElementById('sort-select');
  if (sortSelect) {
    sortSelect.addEventListener('change', function() {
      // Sortier-Logik hier implementieren
      console.log('Sortierung geändert zu:', this.value);
    });
  }

  // Initiale Anzeige aller Fische
  updateResultsCount();
});
</script>
