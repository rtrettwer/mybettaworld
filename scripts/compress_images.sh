#!/bin/bash

# Backup-Ordner anlegen
mkdir -p assets_backup
cp -r ../docs/assets/* assets_backup/

# JPG und PNG komprimieren
find ../docs/assets/ -type f \( -iname "*.jpg" -o -iname "*.jpeg" \) -exec mogrify -strip -interlace Plane -quality 85% {} \;
find ../docs/assets/ -type f -iname "*.png" -exec mogrify -strip -quality 85 {} \;

# Optional: Nach WebP konvertieren (ImageMagick muss WebP unterstützen)
 find ../docs/assets/ -type f \( -iname "*.jpg" -o -iname "*.png" \) -exec sh -c 'cwebp -q 80 "$0" -o "${0%.*}.webp"' {} \;

echo "Bilder wurden komprimiert. Backup liegt in assets_backup/"
