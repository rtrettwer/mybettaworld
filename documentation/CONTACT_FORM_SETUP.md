# Kontaktformular Setup mit Formspree

## Übersicht

Das Kontaktformular verwendet **Formspree**, einen kostenlosen Service für statische Websites, der E-Mails im Hintergrund versendet, ohne dass deine E-Mail-Adresse öffentlich sichtbar ist.

## Setup-Schritte

### 1. Formspree-Account erstellen

1. Gehe zu [formspree.io](https://formspree.io)
2. Erstelle einen kostenlosen Account (50 Submissions/Monat inklusive)
3. Bestätige deine E-Mail-Adresse

### 2. Neues Formular erstellen

1. Klicke auf "New Form"
2. Gib einen Namen ein (z.B. "MyBettaWorld Contact")
3. Wähle deine E-Mail-Adresse aus (themorethebetta@trettwer.de)
4. Kopiere die **Form ID** (sieht aus wie: `xyzabc123`)

### 3. Form ID in die Website einfügen

Ersetze in der Datei `docs/_includes/contact_form.html` die Zeile:

```html
<form id="contactForm" action="https://formspree.io/f/YOUR_FORM_ID" method="POST"></form>
```

Mit deiner echten Form ID:

```html
<form id="contactForm" action="https://formspree.io/f/xyzabc123" method="POST"></form>
```

### 4. Formspree konfigurieren (Optional)

Im Formspree-Dashboard kannst du:

- **Auto-Reply aktivieren**: Automatische Bestätigungsmail an den Absender
- **Spam-Schutz aktivieren**: reCAPTCHA hinzufügen
- **Benachrichtigungen anpassen**: E-Mail-Vorlagen bearbeiten
- **Submissions anzeigen**: Alle eingegangenen Nachrichten einsehen

## Funktionsweise

### Für Besucher

1. Klick auf "Kontakt aufnehmen" bei einem Fisch oder im Footer
2. Formular öffnet sich mit vorausgefüllten Informationen
3. Besucher gibt nur seine E-Mail-Adresse ein (Pflichtfeld)
4. Nach dem Absenden: Erfolgs- oder Fehlermeldung
5. Formular schließt sich automatisch nach 3 Sekunden

### Für dich

1. Du erhältst eine E-Mail an themorethebetta@trettwer.de
2. Die E-Mail enthält:
   - Betreff (z.B. "Interesse an: Jungfisch M01")
   - Produkt-Informationen
   - Nachricht des Besuchers
   - E-Mail-Adresse des Besuchers (für Antwort)

## Vorausgefüllte Formulare

Das Formular wird automatisch vorausgefüllt, wenn jemand auf einen Fisch klickt:

```javascript
openContactForm("Jungfisch M01", "Männchen", "15€");
```

Das Formular zeigt dann:

- **Betreff**: "Interesse an: Jungfisch M01 (Männchen)"
- **Produkt**: "Jungfisch M01 - Typ: Männchen - Preis: 15€"
- **Nachricht**: Vorausgefüllte Vorlage

## Implementierte Features

### Spam-Schutz

- **Honeypot-Feld**: Unsichtbares Feld, das Bots ausfüllen
- **Formspree SPAM-Filter**: Automatischer Schutz

### Benutzerfreundlichkeit

- **Vorausgefüllte Felder**: Bei Interesse an einem Artikel
- **Pflichtfeld nur E-Mail**: Minimaler Aufwand für Besucher
- **Ladezustand**: "Wird gesendet..." während des Versendens
- **Erfolgs-/Fehlermeldungen**: Klares Feedback
- **Keyboard-Support**: ESC zum Schließen
- **Responsive Design**: Funktioniert auf allen Geräten

### Datenschutz

- Deine E-Mail-Adresse ist nicht im Quellcode sichtbar
- Nur Formspree kennt deine E-Mail-Adresse
- Datenschutz-Hinweis im Formular

## Kosten

### Kostenloser Plan (aktuell)

- 50 Submissions pro Monat
- Basis Spam-Schutz
- E-Mail-Benachrichtigungen
- 7 Tage Submission-Speicherung

### Bezahlte Pläne (optional)

- **Gold ($10/Monat)**: 1.000 Submissions, reCAPTCHA, unbegrenzte Speicherung
- **Platinum ($40/Monat)**: 10.000 Submissions, Premium Support

## Alternativen zu Formspree

Falls du später wechseln möchtest:

1. **Netlify Forms**: Wenn du zu Netlify wechselst
2. **EmailJS**: Ähnlich wie Formspree
3. **Google Forms**: Kostenlos, aber weniger flexibel
4. **Eigener Server**: Benötigt Backend-Programmierung

## Dateien

Das Kontaktformular besteht aus:

- `docs/_includes/contact_form.html` - HTML-Markup
- `docs/assets/js/contact-form.js` - JavaScript-Funktionalität
- `docs/assets/_contact-form.scss` - Styling
- `docs/_layouts/default.html` - Integration

## Troubleshooting

### Formular sendet nicht

- Prüfe die Form ID in `contact_form.html`
- Schaue in der Browser-Konsole nach Fehlern
- Prüfe Formspree-Dashboard auf Fehler

### Keine E-Mails ankommen

- Prüfe Spam-Ordner
- Bestätige E-Mail-Adresse in Formspree
- Prüfe Formspree-Dashboard auf Status

### Formular öffnet nicht

- Prüfe Browser-Konsole auf JavaScript-Fehler
- Stelle sicher, dass `contact-form.js` geladen wird
- Prüfe, ob Adblocker das Skript blockiert

## Support

- **Formspree Docs**: https://help.formspree.io
- **Formspree Support**: support@formspree.io

## Nächste Schritte

1. ✅ Formspree-Account erstellen
2. ✅ Form ID einfügen
3. ✅ Testen mit echter E-Mail
4. ✅ Auto-Reply konfigurieren (optional)
5. ✅ Spam-Schutz aktivieren (optional)
