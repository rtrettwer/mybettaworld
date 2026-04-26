#!/usr/bin/env python3
"""
Berechnet die Statistiken für die Startseite (index.md) neu und trägt sie ein.
Gezählt werden Fisch-Profile, aktive Becken, Zucht-Einträge,
aktive Laichungen und behaltene Betta-Weibchen.
"""

import os
import re
import yaml

_SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
POSTS_DIR = os.path.join(_SCRIPT_DIR, "../docs/_posts")
INDEX_FILE = os.path.join(_SCRIPT_DIR, "../docs/index.md")


def parse_frontmatter(filepath):
    """Liest nur den YAML-Frontmatter eines Markdown-Posts."""
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    if not content.startswith("---"):
        return {}
    parts = content.split("---", 2)
    if len(parts) < 3:
        return {}
    try:
        return yaml.safe_load(parts[1]) or {}
    except yaml.YAMLError:
        return {}


def parse_all_posts():
    posts = []
    for fname in os.listdir(POSTS_DIR):
        if not fname.endswith(".md"):
            continue
        fm = parse_frontmatter(os.path.join(POSTS_DIR, fname))
        fm["_filename"] = fname
        posts.append(fm)
    return posts


def normalize_list(value):
    """Stellt sicher, dass ein Frontmatter-Wert als Liste zurückgegeben wird."""
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value]
    return [str(value).strip()]


def compute_stats(posts):
    total_posts = len(posts)

    fish_posts = [p for p in posts if "fish" in normalize_list(p.get("categories"))]
    fish_count = len(fish_posts)

    tank_posts = [p for p in posts if "tank" in normalize_list(p.get("categories"))]
    active_tanks = [t for t in tank_posts if t.get("aktiv") is True]
    active_tank_count = len(active_tanks)

    breeding_posts = [
        p
        for p in posts
        if "zucht" in normalize_list(p.get("tags"))
        or "breeding" in normalize_list(p.get("categories"))
    ]
    breeding_count = len(breeding_posts)

    # Aktive Laichungen: aktive Tank-Posts mit Tag "aktive_laichung"
    # Dieser Tag wird manuell gesetzt solange Jungfische vorhanden sind.
    active_spawning = [
        t
        for t in active_tanks
        if "aktive_laichung" in normalize_list(t.get("tags"))
    ]
    active_spawning_count = len(active_spawning)

    # Behaltene Betta-Weibchen: fish_gender Weiblich, kein fish_status sold/deceased
    def is_female(p):
        gender = str(p.get("fish_gender", "")).strip().lower()
        fish_type = str(p.get("fish_type", "")).strip().lower()
        return "weib" in gender or "weibchen" in fish_type

    def is_active_fish(p):
        status = str(p.get("fish_status", "")).strip().lower()
        return status not in ("sold", "deceased", "verkauft", "gestorben", "tot")

    kept_females = [p for p in fish_posts if is_female(p) and is_active_fish(p)]
    kept_females_count = len(kept_females)

    return {
        "total_posts": total_posts,
        "fish_count": fish_count,
        "active_tank_count": active_tank_count,
        "breeding_count": breeding_count,
        "active_spawning_count": active_spawning_count,
        "kept_females_count": kept_females_count,
    }


def update_index(stats):
    with open(INDEX_FILE, encoding="utf-8") as f:
        content = f.read()

    original = content

    # Hardcodierte Zahlen ersetzen (nur in den bekannten stat-Blöcken)
    # Aktive Laichungen
    content = re.sub(
        r'(<div class="stat-number">)\s*\d+\s*(</div>\s*<div class="stat-label">Aktive Laichungen</div>)',
        rf'\g<1>{stats["active_spawning_count"]}\g<2>',
        content,
    )

    # Betta-Weibchen behalten
    content = re.sub(
        r'(<div class="stat-number">)\s*\d+\s*(</div>\s*<div class="stat-label">Betta-Weibchen behalten</div>)',
        rf'\g<1>{stats["kept_females_count"]}\g<2>',
        content,
    )

    if content == original:
        print("ℹ️  Keine Änderungen nötig – Zahlen bereits aktuell.")
    else:
        with open(INDEX_FILE, "w", encoding="utf-8") as f:
            f.write(content)
        print("✅ index.md aktualisiert.")

    return content != original


def main():
    posts = parse_all_posts()
    stats = compute_stats(posts)

    print("📊 Berechnete Statistiken:")
    print(f"  Blog-Einträge gesamt:     {stats['total_posts']}")
    print(f"  Fisch-Profile:            {stats['fish_count']}")
    print(f"  Aktive Becken:            {stats['active_tank_count']}")
    print(f"  Zucht-Einträge:           {stats['breeding_count']}")
    print(f"  Aktive Laichungen:        {stats['active_spawning_count']}")
    print(f"  Betta-Weibchen behalten:  {stats['kept_females_count']}")

    print()
    update_index(stats)

    # Hinweis zu Liquid-berechneten Werten
    print()
    print("ℹ️  Folgende Werte werden bereits dynamisch per Jekyll/Liquid berechnet")
    print("   und müssen NICHT manuell gepflegt werden:")
    print("   → Blog-Einträge, Fisch-Profile, Aktive Becken, Zucht-Einträge")


if __name__ == "__main__":
    main()
