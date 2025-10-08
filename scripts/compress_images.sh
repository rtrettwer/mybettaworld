#!/bin/bash

## Backup-Ordner anlegen
mkdir -p assets_backup
cp -r ../docs/assets/* assets_backup/

## Thumbnails-Ordner anlegen
mkdir -p ../docs/assets/thumbnails

## Für jedes Bild ein Thumbnail (300px breit, WebP) erzeugen
find ../docs/assets/ -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" \) | while read img; do
  # Zielpfad für Thumbnail (immer .webp)
  relpath="${img#../docs/assets/}"
  thumb="../docs/assets/thumbnails/${relpath%.*}.webp"
  mkdir -p "$(dirname "$thumb")"
  # Thumbnail erzeugen, falls nicht vorhanden
  if [ ! -f "$thumb" ]; then
    cwebp -resize 300 0 -q 80 "$img" -o "$thumb"
  fi
done

## JPG und PNG komprimieren
find ../docs/assets/ -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) -exec mogrify -strip -interlace Plane -quality 85% {} \;
find ../docs/assets/ -type f -iname "*.png" -exec mogrify -strip -quality 85 {} \;

## Optional: Nach WebP konvertieren (ImageMagick muss WebP unterstützen)
# find ../docs/assets/ -type f \( -iname "*.jpg" -o -iname "*.png" \) -exec sh -c 'cwebp -q 80 "$0" -o "${0%.*}.webp"' {} \;

echo "Bilder wurden komprimiert und WebP-Thumbnails erzeugt. Backup liegt in assets_backup/"
