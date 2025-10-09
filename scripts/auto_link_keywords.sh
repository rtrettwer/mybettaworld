#!/bin/bash
# Automatisches Verlinken von Begriffen in Markdown-Posts anhand einer YAML-Mapping-Datei
# keywords.yml Format:
# - key: Lila
#   url: /fish/lila/

MAPPING_FILE="$(dirname "$0")/keywords.yml"
POSTS_DIR="$(dirname "$0")/../docs/_posts"

if [ ! -f "$MAPPING_FILE" ]; then
  echo "Mapping-Datei $MAPPING_FILE nicht gefunden!"
  exit 1
fi

# YAML parsen: key und url extrahieren
parse_yaml() {
  awk '/^- key:/ {key=$3} /url:/ {url=$2; print key"|"url}' "$MAPPING_FILE"
}

parse_yaml | while IFS='|' read -r KEY URL; do
  [[ -z "$KEY" || -z "$URL" ]] && continue
  for FILE in "$POSTS_DIR"/*.md; do
    # Extrahiere fish_name oder title aus dem Front Matter
    OWN_NAME=$(awk 'BEGIN{found=0} /^---[ ]*$/ {found++; next} found==1 && ($1=="fish_name:"||$1=="title:") {for(i=2;i<=NF;i++) printf $i " "; print ""; exit}' "$FILE" | sed 's/ *$//')
    if [ -z "$OWN_NAME" ]; then
      FILENAME=$(basename "$FILE")
      OWN_NAME=$(echo "$FILENAME" | sed -E 's/^[0-9\-]+(fish|tank)_//; s/\.md$//; s/_/ /g; s/.*/\u&/')
    fi
    OWN_NAME_LC=$(echo "$OWN_NAME" | tr '[:upper:]' '[:lower:]' | xargs)
    KEY_LC=$(echo "$KEY" | tr '[:upper:]' '[:lower:]' | xargs)
    if [ "$OWN_NAME_LC" = "$KEY_LC" ]; then
      echo "Überspringe Selbstverlinkung: $KEY in $(basename "$FILE")"
      continue
    fi
    TMPFILE="${FILE}.tmp_autolink"
    # Maskiere bereits verlinkte Begriffe, ersetze dann alle übrigen exakten Vorkommen, stelle Links wieder her
    awk -v key="$KEY" -v url="$URL" '
      BEGIN { repl="["key"]("url")"; frontmatter_count=0; mask="__ALREADY_LINKED__" }
      {
        if ($0 ~ /^---[ ]*$/) { frontmatter_count++; print; next }
        if (frontmatter_count < 2) { print }
        else {
          line = $0
          # Maskiere bereits verlinkte Begriffe
          gsub("\\["key"\\]\\([^)]+\\)", mask, line)
          # Ersetze exakte, nicht verlinkte Begriffe (Wortgrenzen, keine Gruppenreferenzen)
          # Nur für GNU awk: gsub("\\<"key"\\>", repl, line)
          # Für POSIX awk (macOS): split und wieder zusammensetzen
          n = split(line, arr, /([^A-Za-z0-9_]+)/, seps)
          out = ""
          for (i = 1; i <= n; i++) {
            if (arr[i] == key) arr[i] = repl
            out = out arr[i]
            if (i < n) out = out seps[i]
          }
          # Maskierte Links zurückwandeln
          gsub(mask, "["key"]("url")", out)
          print out
        }
      }
    ' "$FILE" > "$TMPFILE"
    mv "$TMPFILE" "$FILE"
    echo "Verlinkt: $KEY in $(basename "$FILE")"
  done
done
echo "Fertig."
