---
layout: default
title: "Über mich"
permalink: /about/
---

<div class="blog-container">
  <div class="blog-header-card content-card">
    <h1>Über mich</h1>
    <p>Lerne die Person hinter diesem Blog kennen</p>
  </div>

  <div class="content-card">
    <p>Hallo! Ich bin Software-Entwicklerin und seit diesem Jahr auch begeisterte Aquarianerin. Besonders fasziniert mich die Haltung und Zucht von siamesischen Kampffischen (betta splendens).</p>

    <p>Neben meiner Leidenschaft für Technik und Programmierung widme ich mich mit großer Freude meinen Aquarien, die ich möglichst naturnah und im LowTech-Stil pflege. Das bedeutet: wenig Technik, viel Natur und ein harmonisches Gleichgewicht zwischen Pflanzen und Tieren.</p>

    <p>Ich wohne südlich von München in einer gemütlichen kleinen Wohnung, die ich mit meinen Fischen und zahlreichen Pflanzen teile. Hier auf dem Blog dokumentiere ich meine Erfahrungen, Erfolge und Herausforderungen rund um meine Aquarien und Betta-Fische.</p>

  </div>

  <!-- Klickbarer Logo-Fisch mit Sprechblase -->
  <div class="jingle-fish-wrap">
    <button class="jingle-fish-btn" onclick="window.playBettaJingle && window.playBettaJingle()" aria-label="Jingle abspielen">
      <span class="jingle-bubble">Drück mich! 🎵</span>
      <img src="{{ '/assets/images/misc/icon.webp' | relative_url }}" alt="Betta Logo" class="jingle-fish-img" />
    </button>
  </div>
</div>

<style>
  .jingle-fish-wrap {
    display: flex;
    justify-content: center;
    margin: 2rem 0 1rem;
  }

  .jingle-fish-btn {
    background: none;
    border: none;
    cursor: pointer;
    position: relative;
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.5rem;
    padding: 0;
    transition: transform 0.18s ease;
  }

  .jingle-fish-btn:hover {
    transform: scale(1.07);
  }

  .jingle-fish-btn:active {
    transform: scale(0.96);
  }

  /* Sprechblase */
  .jingle-bubble {
    background: linear-gradient(135deg, var(--theme-primary-1, #2ec4b6), var(--theme-primary-2, #20639b));
    color: #fff;
    font-weight: 700;
    font-size: 0.95rem;
    padding: 0.45rem 1.1rem;
    border-radius: 999px;
    box-shadow: 0 4px 14px rgba(46, 196, 182, 0.35);
    position: relative;
    white-space: nowrap;
    /* kleines Dreieck nach unten zum Fisch */
    margin-bottom: 4px;
  }

  .jingle-bubble::after {
    content: "";
    position: absolute;
    bottom: -8px;
    left: 50%;
    transform: translateX(-50%);
    border: 5px solid transparent;
    border-top-color: var(--theme-primary-2, #20639b);
  }

  /* Fisch-Bild */
  .jingle-fish-img {
    width: 120px;
    height: auto;
    filter: drop-shadow(0 4px 12px rgba(46, 196, 182, 0.4));
    transition: filter 0.2s ease;
  }

  .jingle-fish-btn:hover .jingle-fish-img {
    filter: drop-shadow(0 6px 18px rgba(46, 196, 182, 0.65));
  }

  /* Wackeln nach dem Klick */
  @keyframes fish-wiggle {
    0%   { transform: rotate(0deg); }
    20%  { transform: rotate(-8deg); }
    40%  { transform: rotate(7deg); }
    60%  { transform: rotate(-5deg); }
    80%  { transform: rotate(3deg); }
    100% { transform: rotate(0deg); }
  }

  .jingle-fish-img.wiggle {
    animation: fish-wiggle 0.5s ease;
  }
</style>

<script>
  (function () {
    const btn = document.querySelector(".jingle-fish-btn");
    const img = document.querySelector(".jingle-fish-img");
    if (btn && img) {
      btn.addEventListener("click", function () {
        img.classList.remove("wiggle");
        void img.offsetWidth; // reflow für Neustart
        img.classList.add("wiggle");
        img.addEventListener("animationend", () => img.classList.remove("wiggle"), { once: true });
      });
    }
  })();
</script>

{% include betta_jingle.html %}
