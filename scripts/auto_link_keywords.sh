#!/bin/bash
# Automatisches Verlinken von Begriffen in Markdown-Posts anhand einer Mapping-Datei
# keywords.txt Format: Begriff|URL

MAPPING_FILE="$(dirname "$0")/keywords.txt"
POSTS_DIR="$(dirname "$0")/../docs/_posts"

if [ ! -f "$MAPPING_FILE" ]; then
  echo "Mapping-Datei $MAPPING_FILE nicht gefunden!"
  exit 1
fi

while IFS='|' read -r KEY URL; do
  # Leere oder Kommentarzeilen überspringen
  [[ -z "$KEY" || "$KEY" =~ ^# ]] && continue
  # Für jede Markdown-Datei
  for FILE in "$POSTS_DIR"/*.md; do
    # Nur ersetzen, wenn der Begriff nicht schon verlinkt ist
    # Sucht nach KEY, das nicht in []() steht
    TMPFILE="${FILE}.tmp_autolink"
    awk -v key="$KEY" -v url="$URL" '
      BEGIN { repl="["key"]("url")" }
      {
        # Nur ersetzen, wenn key nicht schon in []() steht
        gsub("(^|[^\\[])("key")([^\\]]|$)", "\\1"repl"\\3")
        print
      }
    ' "$FILE" > "$TMPFILE"
    mv "$TMPFILE" "$FILE"
    echo "Verlinkt: $KEY in $(basename "$FILE")"
  done
done < "$MAPPING_FILE"
echo "Fertig."
Betta splendens|/fish/betta-splendens/
Artemia|/food/artemia/
Essigälchen|/food/essigaelchen/

