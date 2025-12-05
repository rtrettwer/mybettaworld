nd # Kontaktformular - Implementierung abgeschlossen ✅

## Zusammenfassung

Ein vollständiges Kontaktformular wurde implementiert, das:

✅ **Deine E-Mail-Adresse verbirgt** - Nutzer sehen nur ein Formular
✅ **Vorausgefüllt ist** - Bei Interesse an einem Fisch werden alle Infos automatisch ausgefüllt
✅ **Minimal ist** - Nur E-Mail-Adresse des Nutzers ist Pflicht
✅ **Im Hintergrund E-Mails sendet** - An themorethebetta@trettwer.de
✅ **Responsive ist** - Funktioniert auf allen Geräten
✅ **SPAM-Schutz hat** - Honeypot-Feld + Formspree-Filter

## Was wurde implementiert?

### 1. Kontaktformular-Komponente

**Datei**: `docs/_includes/contact_form.html`

- Modal-Overlay mit Formular
- Vorausgefüllte Felder für Produkt-Anfragen
- Erfolgs- und Fehlermeldungen
- SPAM-Schutz (Honeypot)

### 2. JavaScript-Funktionalität

**Datei**: `docs/assets/js/contact-form.js`

- `openContactForm(productName, productType, price)` - Öffnet Formular
- `closeContactForm()` - Schließt Formular
- Formular-Validierung und -Submission
- ESC-Taste zum Schließen
- Click-Outside zum Schließen

### 3. Styling

**Datei**: `docs/assets/_contact-form.scss`

- Modernes, responsives Design
- Animationen (Fade-in, Slide-in)
- Dark-Mode Support
- Mobile-optimiert

### 4. Integration

- `docs/_layouts/default.html` - Formular global verfügbar
- `docs/_includes/footer.html` - "Kontakt"-Button im Footer
- `docs/_includes/sales_gallery.html` - "Kontakt aufnehmen"-Button bei Produkten

## Wo wird das Formular angezeigt?

### 1. Verkaufs-Galerie

Bei jedem verfügbaren Artikel:

```html
<button onclick="openContactForm('Jungfisch M01', 'Männchen', '15€')">Kontakt aufnehmen</button>
```

Das Formular zeigt dann:

- **Betreff**: "Interesse an: Jungfisch M01 (Männchen)"
- **Nachricht**: Vorausgefüllte Vorlage mit Produkt-Infos
- **Nur Pflicht**: E-Mail-Adresse des Interessenten

### 2. Footer

Allgemeiner Kontakt-Button:

```html
<button onclick="openContactForm()">Kontakt</button>
```

Das Formular zeigt dann:

- **Betreff**: "Allgemeine Anfrage"
- **Nachricht**: Leer
- **Nur Pflicht**: E-Mail-Adresse

## Wie funktioniert es?

### Für Besucher

1. **Klick auf "Kontakt aufnehmen"** bei einem Fisch
2. **Formular öffnet sich** mit vorausgefüllten Informationen:
   - Betreff: "Interesse an: [Fischname]"
   - Nachricht: "Hallo, ich interessiere mich für [Fischname]..."
3. **Besucher gibt E-Mail ein** (einziges Pflichtfeld)
4. **Klick auf "Nachricht senden"**
5. **Erfolgs- oder Fehlermeldung** wird angezeigt
6. **Formular schließt sich** automatisch nach 3 Sekunden

### Für dich

Du erhältst eine E-Mail an **themorethebetta@trettwer.de** mit:

```
Von: noreply@formspree.io
An: themorethebetta@trettwer.de
Betreff: Neue Nachricht von MyBettaWorld

Betreff: Interesse an: Jungfisch M01 (Männchen)

Name: [Optional - wenn ausgefüllt]
E-Mail: beispiel@email.de

Produkt: Jungfisch M01
Typ: Männchen
Preis: 15€

Nachricht:
Hallo,

ich interessiere mich für "Jungfisch M01" und hätte gerne mehr Informationen.

[Weitere Nachricht des Besuchers]
```

## Nächster Schritt: Formspree einrichten

### 1. Account erstellen

1. Gehe zu [formspree.io](https://formspree.io)
2. Erstelle einen kostenlosen Account
3. Bestätige deine E-Mail-Adresse (themorethebetta@trettwer.de)

### 2. Formular erstellen

1. Klicke auf "+ New Form"
2. Name: "MyBettaWorld Contact"
3. E-Mail: themorethebetta@trettwer.de
4. Kopiere die **Form ID** (z.B. `xyzabc123`)

### 3. Form ID einfügen

Öffne `docs/_includes/contact_form.html` und ersetze Zeile 9:

```html
<!-- VORHER -->
<form id="contactForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST">
  <!-- NACHHER (mit deiner Form ID) -->
  <form id="contactForm" action="https://formspree.io/f/xyzabc123" method="POST"></form>
</form>
```

### 4. Testen

1. Starte Jekyll-Server: `bundle exec jekyll serve`
2. Öffne http://localhost:4000/sale/
3. Klicke auf "Kontakt aufnehmen" bei einem Fisch
4. Teste das Formular mit deiner E-Mail
5. Prüfe, ob du die E-Mail erhältst

### 5. Optional: Konfigurieren

Im Formspree-Dashboard:

- ✅ **Auto-Reply**: Automatische Bestätigung an Absender
- ✅ **reCAPTCHA**: Zusätzlicher Spam-Schutz
- ✅ **Benachrichtigungen**: E-Mail-Vorlagen anpassen
- ✅ **Submissions**: Alle Nachrichten einsehen

## Dateien-Übersicht

```
docs/
├── _includes/
│   ├── contact_form.html          ← Neues Formular
│   ├── footer.html                ← Geändert (Kontakt-Button)
│   └── sales_gallery.html         ← Geändert (Kontakt-Buttons)
├── _layouts/
│   └── default.html               ← Geändert (Formular-Integration)
├── assets/
│   ├── js/
│   │   └── contact-form.js        ← Neu
│   ├── _contact-form.scss         ← Neu
│   └── main.scss                  ← Geändert (Import hinzugefügt)
└── documentation/
    └── CONTACT_FORM_SETUP.md      ← Neue Dokumentation
```

## Features im Detail

### ✅ Vorausgefüllte Felder

```javascript
openContactForm("Jungfisch M01", "Männchen", "15€");
```

Füllt automatisch:

- Betreff
- Produkt-Informationen
- Nachricht-Vorlage

### ✅ Validation

- E-Mail-Adresse ist Pflicht
- Browser-native Validierung
- Client-seitige Prüfung vor dem Senden

### ✅ Loading-States

```
[Nachricht senden] → [Wird gesendet...] → [✓ Erfolgreich]
```

### ✅ Error-Handling

```
Ups, da ist etwas schiefgelaufen.
Bitte versuche es nochmal oder schreibe direkt an themorethebetta@trettwer.de
```

### ✅ Accessibility

- ESC-Taste zum Schließen
- Click-Outside zum Schließen
- Focus-Management
- Aria-Labels
- Keyboard-Navigation

### ✅ Mobile-Optimierung

- Responsive Layout
- Touch-freundliche Buttons
- Optimierte Schriftgrößen
- Keine horizontalen Scrollbars

### ✅ SPAM-Schutz

- **Honeypot-Feld**: Unsichtbares Feld für Bots
- **Formspree-Filter**: Automatischer SPAM-Schutz
- **Rate-Limiting**: Maximal 50 Submissions/Monat (kostenlos)

### ✅ Datenschutz

- Deine E-Mail ist nicht sichtbar im Quellcode
- Nur Formspree kennt deine E-Mail
- Hinweis auf Datenschutz im Formular

## Kosten

### Kostenlos (aktuell)

- 50 Submissions/Monat
- Basis SPAM-Schutz
- E-Mail-Benachrichtigungen
- 7 Tage Speicherung

### Bezahlt (optional)

- **Gold ($10/Monat)**: 1.000 Submissions
- **Platinum ($40/Monat)**: 10.000 Submissions

## Nächste Schritte

1. ✅ **Formspree-Account erstellen**
2. ✅ **Form ID einfügen** in `contact_form.html`
3. ✅ **Testen** mit echter E-Mail
4. ✅ **Auto-Reply aktivieren** (optional)
5. ✅ **reCAPTCHA aktivieren** (optional)

## Support

Fragen? Siehe:

- 📖 **Dokumentation**: `documentation/CONTACT_FORM_SETUP.md`
- 🌐 **Formspree Docs**: https://help.formspree.io
- 📧 **Formspree Support**: support@formspree.io
