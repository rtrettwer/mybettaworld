---
layout: page
title: Impressum
permalink: /impressum/
# Impressum-Daten
owner_name: "Rike Trettwer"
address: "Hauptstraße 31a"
postal_code: "82008"
city: "Unterhaching"
country: "Deutschland"
email: "rike@trettwer.de"
---

<div style="margin: 2rem 0;">
  <div style="margin: 2rem 0; text-align: left; max-width: 800px; margin-left: auto; margin-right: auto;">
    
    <h2>Angaben gemäß § 5 TMG</h2>
    
    <div style="margin: 1.5rem 0;">
      <h3>Verantwortlich für den Inhalt</h3>
      <p>
        <strong>{{ page.owner_name }}</strong><br>
        {{ page.address }}<br>
        {{ page.postal_code }} {{ page.city }}<br>
        {{ page.country }}
      </p>
    </div>
    
    <div style="margin: 1.5rem 0;">
      <h3>Kontakt</h3>
      <p>
        E-Mail: {{ page.email }}<br>
        {% if page.phone %}Telefon: {{ page.phone }}{% endif %}
      </p>
    </div>
    
    <div style="margin: 1.5rem 0;">
      <h3>Haftungsausschluss</h3>
      
      <h4>Haftung für Inhalte</h4>
      <p>
        Als Diensteanbieter sind wir gemäß § 7 Abs.1 TMG für eigene Inhalte auf diesen Seiten nach den allgemeinen Gesetzen verantwortlich. Nach §§ 8 bis 10 TMG sind wir als Diensteanbieter jedoch nicht unter der Verpflichtung, übermittelte oder gespeicherte fremde Informationen zu überwachen oder nach Umständen zu forschen, die auf eine rechtswidrige Tätigkeit hinweisen.
      </p>
      
      <h4>Haftung für Links</h4>
      <p>
        Unser Angebot enthält Links zu externen Websites Dritter, auf deren Inhalte wir keinen Einfluss haben. Deshalb können wir für diese fremden Inhalte auch keine Gewähr übernehmen. Für die Inhalte der verlinkten Seiten ist stets der jeweilige Anbieter oder Betreiber der Seiten verantwortlich.
      </p>
      
      <h4>Urheberrecht</h4>
      <p>
        Die durch die Seitenbetreiber erstellten Inhalte und Werke auf diesen Seiten unterliegen dem deutschen Urheberrecht. Die Vervielfältigung, Bearbeitung, Verbreitung und jede Art der Verwertung außerhalb der Grenzen des Urheberrechtes bedürfen der schriftlichen Zustimmung des jeweiligen Autors bzw. Erstellers.
      </p>
    </div>
  </div>
</div>

<style>
h2 {
  color: var(--theme-green, #4CAF50);
  border-bottom: 2px solid var(--theme-blue, #2196F3);
  padding-bottom: 0.5rem;
}

h3 {
  color: var(--theme-blue, #2196F3);
  margin-top: 2rem;
}

h4 {
  color: var(--theme-green, #4CAF50);
  margin-top: 1.5rem;
}
</style>
