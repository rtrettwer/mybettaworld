#!/bin/bash
# Löscht Thumbnails, für die kein passendes Originalbild existiert
# Thumbnail: assets/thumbnails/foo_thumb.webp → Original: assets/{fish,food,tanks,misc}/foo.webp|jpg|png

THUMB_DIR="$(dirname "$0")/../docs/assets/thumbnails"
ASSETS_DIR="$(dirname "$0")/../docs/assets"

for thumb in "$THUMB_DIR"/*_thumb.*; do
  [ -e "$thumb" ] || continue
  base=$(basename "$thumb")
  name_ext="${base%_thumb.*}"
  found=0
  for sub in fish food tanks misc; do
    for ext in webp jpg jpeg png; do
      if [ -f "$ASSETS_DIR/$sub/$name_ext.$ext" ]; then
        found=1
        break 2
      fi
    done
  done
  if [ $found -eq 0 ]; then
    echo "Lösche Thumbnail ohne Original: $thumb"
    rm "$thumb"
  fi
done

