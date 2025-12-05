// Verkaufs-Galerie Filterfunktion - Verbesserte Version
(function () {
  "use strict";

  let activeFilters = {
    gender: "all",
    status: "all",
    maxPrice: 200,
    search: "",
  };

  let fishCards = [];
  let filterButtons = [];

  function initializeFilters() {
    // Warte bis DOM vollständig geladen ist
    if (document.readyState === "loading") {
      document.addEventListener("DOMContentLoaded", initializeFilters);
      return;
    }

    console.log("Initialisiere Filterfunktion...");

    filterButtons = document.querySelectorAll(".filter-btn");
    fishCards = document.querySelectorAll(".fish-card");

    console.log("Gefundene Filter-Buttons:", filterButtons.length);
    console.log("Gefundene Fish-Cards:", fishCards.length);

    if (filterButtons.length === 0 || fishCards.length === 0) {
      console.warn("Keine Filter-Buttons oder Fish-Cards gefunden. Versuche erneut in 500ms...");
      setTimeout(initializeFilters, 500);
      return;
    }

    setupFilterButtons();
    setupAdvancedFilters();
    setupInterestButtons();
    setupSortFunction();

    // Initiale Anzeige
    applyAllFilters();

    console.log("Filterfunktion erfolgreich initialisiert!");
  }

  function setupFilterButtons() {
    filterButtons.forEach((button) => {
      button.addEventListener("click", function (e) {
        e.preventDefault();
        console.log("Filter-Button geklickt:", this.getAttribute("data-filter"));

        // Entferne aktive Klasse von allen Buttons
        filterButtons.forEach((btn) => btn.classList.remove("active"));
        // Füge aktive Klasse zum geklickten Button hinzu
        this.classList.add("active");

        const filterValue = this.getAttribute("data-filter");
        activeFilters.gender = filterValue;
        applyAllFilters();
      });
    });
  }

  function setupAdvancedFilters() {
    // Status-Filter
    const statusFilter = document.querySelector("#status-filter");
    if (statusFilter) {
      statusFilter.addEventListener("change", function () {
        console.log("Status-Filter geändert:", this.value);
        activeFilters.status = this.value;
        applyAllFilters();
      });
    }

    // Preis-Range Filter
    const priceRange = document.querySelector("#price-range");
    const priceDisplay = document.querySelector("#price-display");
    if (priceRange) {
      priceRange.addEventListener("input", function () {
        const price = parseInt(this.value);
        activeFilters.maxPrice = price;
        if (priceDisplay) {
          priceDisplay.textContent = price + "€";
        }
        applyAllFilters();
      });
    }

    // Suchfeld
    const searchInput = document.querySelector("#search-fish");
    if (searchInput) {
      let searchTimeout;
      searchInput.addEventListener("input", function () {
        clearTimeout(searchTimeout);
        searchTimeout = setTimeout(() => {
          console.log("Suche:", this.value);
          activeFilters.search = this.value.toLowerCase();
          applyAllFilters();
        }, 300);
      });
    }

    // Sortierung
    const sortSelect = document.querySelector("#sort-select");
    if (sortSelect) {
      sortSelect.addEventListener("change", function () {
        console.log("Sortierung geändert:", this.value);
        sortFish(this.value);
        updateResultsCount();
      });
    }
  }

  function setupInterestButtons() {
    const interestButtons = document.querySelectorAll(".interest-btn:not([disabled])");
    interestButtons.forEach((button) => {
      button.addEventListener("click", function (e) {
        e.preventDefault();
        const fishCard = this.closest(".fish-card");
        const fishName = fishCard.querySelector("h4").textContent;

        // E-Mail Link erstellen
        const subject = encodeURIComponent(`Interesse an Betta-Fisch: ${fishName}`);
        const body = encodeURIComponent(
          `Hallo,\n\nich interessiere mich für den Betta-Fisch "${fishName}" aus Ihrer Verkaufsanzeige.\n\nBitte kontaktieren Sie mich für weitere Details.\n\nVielen Dank!`
        );
        const mailtoLink = `mailto:info@trettwer.de?subject=${subject}&body=${body}`;

        window.location.href = mailtoLink;
      });
    });
  }

  function applyAllFilters() {
    console.log("Wende Filter an:", activeFilters);
    let visibleCount = 0;

    fishCards.forEach((card) => {
      const category = card.getAttribute("data-category") || "";
      const status = card.getAttribute("data-status") || "";
      const price = parseInt(card.getAttribute("data-price")) || 0;

      // Text-Inhalte für Suche
      const nameElement = card.querySelector("h4");
      const descriptionElement = card.querySelector(".description");
      const colorElement = card.querySelector(".color");

      const name = nameElement ? nameElement.textContent.toLowerCase() : "";
      const description = descriptionElement ? descriptionElement.textContent.toLowerCase() : "";
      const color = colorElement ? colorElement.textContent.toLowerCase() : "";

      let visible = true;

      // Gender Filter
      if (activeFilters.gender !== "all" && category !== activeFilters.gender) {
        visible = false;
      }

      // Status Filter
      if (activeFilters.status !== "all" && status !== activeFilters.status) {
        visible = false;
      }

      // Price Filter
      if (price > activeFilters.maxPrice) {
        visible = false;
      }

      // Search Filter
      if (activeFilters.search && activeFilters.search.length > 0) {
        const searchTerm = activeFilters.search;
        if (!name.includes(searchTerm) && !description.includes(searchTerm) && !color.includes(searchTerm)) {
          visible = false;
        }
      }

      // Apply visibility with animation
      if (visible) {
        card.style.display = "block";
        card.classList.remove("hidden");
        visibleCount++;
      } else {
        card.style.display = "none";
        card.classList.add("hidden");
      }
    });

    console.log("Sichtbare Karten:", visibleCount);
    updateResultsCount();
  }

  function sortFish(sortBy) {
    const fishGrid = document.querySelector(".fish-grid");
    if (!fishGrid) return;

    const cards = Array.from(fishCards);

    cards.sort((a, b) => {
      switch (sortBy) {
        case "price-low":
          return parseInt(a.getAttribute("data-price") || "0") - parseInt(b.getAttribute("data-price") || "0");
        case "price-high":
          return parseInt(b.getAttribute("data-price") || "0") - parseInt(a.getAttribute("data-price") || "0");
        case "name":
          const nameA = a.querySelector("h4")?.textContent || "";
          const nameB = b.querySelector("h4")?.textContent || "";
          return nameA.localeCompare(nameB);
        case "status":
          const statusOrder = { available: 0, reserved: 1, sold: 2 };
          const statusA = a.getAttribute("data-status") || "sold";
          const statusB = b.getAttribute("data-status") || "sold";
          return statusOrder[statusA] - statusOrder[statusB];
        default:
          return 0;
      }
    });

    // Neu sortierte Karten ins Grid einfügen
    cards.forEach((card) => fishGrid.appendChild(card));
  }

  function updateResultsCount() {
    const visibleCards = document.querySelectorAll('.fish-card:not([style*="display: none"])').length;
    const totalCards = fishCards.length;
    const resultsCount = document.getElementById("results-count");
    const noResults = document.getElementById("no-results");

    if (resultsCount) {
      if (visibleCards === 0) {
        resultsCount.textContent = "Keine Ergebnisse";
        if (noResults) noResults.style.display = "block";
      } else {
        resultsCount.textContent = `${visibleCards} von ${totalCards} Fischen`;
        if (noResults) noResults.style.display = "none";
      }
    }
  }

  // Globale Funktionen für HTML
  window.toggleAdvancedFilters = function () {
    const advancedFilters = document.getElementById("advanced-filters");
    if (!advancedFilters) return;

    const isVisible = advancedFilters.style.display !== "none";
    advancedFilters.style.display = isVisible ? "none" : "block";

    const toggleBtn = event.target;
    if (toggleBtn) {
      toggleBtn.textContent = isVisible ? "Erweiterte Filter" : "Filter ausblenden";
    }
  };

  window.resetAllFilters = function () {
    console.log("Filter zurücksetzen");

    // Filter-Buttons zurücksetzen
    filterButtons.forEach((btn) => btn.classList.remove("active"));
    const allButton = document.querySelector('[data-filter="all"]');
    if (allButton) allButton.classList.add("active");

    // Eingabefelder zurücksetzen
    const searchInput = document.getElementById("search-fish");
    const statusFilter = document.getElementById("status-filter");
    const priceRange = document.getElementById("price-range");
    const priceDisplay = document.getElementById("price-display");
    const sortSelect = document.getElementById("sort-select");

    if (searchInput) searchInput.value = "";
    if (statusFilter) statusFilter.value = "all";
    if (priceRange) priceRange.value = "200";
    if (priceDisplay) priceDisplay.textContent = "200€";
    if (sortSelect) sortSelect.value = "name";

    // Filter-State zurücksetzen
    activeFilters = {
      gender: "all",
      status: "all",
      maxPrice: 200,
      search: "",
    };

    applyAllFilters();
  };

  window.showAllFish = function () {
    window.resetAllFilters();
  };

  // Setup-Funktionen für externe Verwendung
  window.setupSortFunction = setupSortFunction;
  function setupSortFunction() {
    window.sortFish = sortFish;
    window.searchFish = function (searchTerm) {
      activeFilters.search = searchTerm.toLowerCase();
      applyAllFilters();
    };
  }

  // Initialisierung starten
  initializeFilters();
})();
