This is my github pages blog on betta caring.

## Features

### Verkaufsgalerie mit Carousel
Die Verkaufsseite unterstützt jetzt Bildergalerien für jeden Artikel. Wenn mehrere Bilder verfügbar sind, werden sie als Carousel angezeigt.

**Verwendung:**
```yaml
# In _data/sales.yml
- name: "Fischname"
  status: "available"
  gender: "male"
  price: 10
  image: "/assets/images/fish/default.webp"  # Fallback-Bild
  gallery:  # Optional: Mehrere Bilder für Carousel
    - "/assets/images/fish/fisch1.webp"
    - "/assets/images/fish/fisch2.webp"
    - "/assets/images/fish/fisch3.webp"
  description: "Beschreibung..."
```

**Funktionen:**
- ✨ Automatisches Carousel bei mehreren Bildern
- 👆 Touch/Swipe-Unterstützung für mobile Geräte
- 🎯 Indikatoren zum direkten Anspringen von Bildern
- ⌨️ Vor/Zurück Buttons beim Hover
- 📱 Responsive Design


