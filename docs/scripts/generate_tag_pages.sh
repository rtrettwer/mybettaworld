#!/bin/bash
# Erzeugt für alle in den Posts verwendeten Tags eine eigene Tag-Seite im Verzeichnis docs/tags/
# Die Seiten nutzen das Layout 'tag_home_blog', das wie die Blog-Startseite aussieht.

POSTS_DIR="$(dirname "$0")/../_posts"
TAGS_DIR="$(dirname "$0")/../tags"
LAYOUT="tag_home_blog"

mkdir -p "$TAGS_DIR"

# Alle Tags aus den Posts extrahieren
TAGS=$(grep -h '^tags:' "$POSTS_DIR"/*.md | sed 's/^tags:[ \[]*//; s/\].*//; s/,/ /g' | tr ' ' '\n' | grep -v '^$' | sort | uniq)

for TAG in $TAGS; do
  SLUG=$(echo "$TAG" | iconv -f utf8 -t ascii//TRANSLIT | tr '[:upper:]' '[:lower:]' | sed 's/ /-/g; s/[^a-z0-9_-]//g')
  cat > "$TAGS_DIR/$SLUG.md" <<EOF
---
layout: $LAYOUT
tag: $TAG
permalink: /tags/$SLUG/
---
EOF
  echo "Erstellt: $TAGS_DIR/$SLUG.md"
done
