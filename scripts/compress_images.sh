#!/bin/bash

## Backup-Ordner anlegen (nur JPG/JPEG-Dateien sichern)
mkdir -p assets_backup
find ../docs/assets/ -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) -exec cp --parents {} assets_backup/ \;

## Thumbnails-Ordner anlegen
mkdir -p ../docs/assets/thumbnails

## Für jedes Bild ein Thumbnail (300px breit, WebP) erzeugen
find ../docs/assets/ -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.webp" \) \
  ! -path "../docs/assets/thumbnails/*" \
  ! -path "../docs/assets_backup/*" \
  | while read img; do
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
find ../docs/assets/ -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) \
  ! -path "../docs/assets/thumbnails/*" \
  ! -path "../docs/assets_backup/*" \
  -exec mogrify -strip -interlace Plane -quality 85% {} \;
find ../docs/assets/ -type f -iname "*.png" \
  ! -path "../docs/assets/thumbnails/*" \
  ! -path "../docs/assets_backup/*" \
  -exec mogrify -strip -quality 85 {} \
;

## Optional: Nach WebP konvertieren (ImageMagick muss WebP unterstützen)
# find ../docs/assets/ -type f \( -iname "*.jpg" -o -iname "*.png" \) \
#   ! -path "../docs/assets/thumbnails/*" \
#   ! -path "../docs/assets_backup/*" \
#   -exec sh -c 'cwebp -q 80 "$0" -o "${0%.*}.webp"' {} \
# ;

echo "Bilder wurden komprimiert und WebP-Thumbnails erzeugt. Backup (nur JPG/JPEG) liegt in assets_backup/"
