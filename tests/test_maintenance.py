import contextlib
import importlib.util
import io
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image
import yaml

ROOT = Path(__file__).resolve().parents[1]


def load_script(name):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts" / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


autolinks = load_script("autolink_posts")
gallery = load_script("sync_gallery_yml")
thumbnails = load_script("generate_thumbnails")


class AutolinkTests(unittest.TestCase):
    def test_preserves_frontmatter_and_is_idempotent(self):
        original = "---\ntitle: Lila\n---\n\nLila trifft Bandit."
        links = {"Lila": "/lila.html", "Bandit": "/bandit.html"}
        expected = "---\ntitle: Lila\n---\n\nLila trifft [Bandit](/bandit.html)."
        actual = autolinks.autolink_content(original, links, "Lila")
        self.assertEqual(expected, actual)
        self.assertEqual(actual, autolinks.autolink_content(actual, links, "Lila"))

    def test_preserves_code_images_links_and_partial_words(self):
        original = (
            "# Lila\n`Lila` ![Lila](/image.webp) [Lila](/custom)\n"
            '<a href="/other">Lila</a> <img alt="Lila" src="/Lila.webp">\n'
            "```text\nLila\n```\nLilaform und SuperLila\n"
        )
        self.assertEqual(original, autolinks.autolink_content(original, {"Lila": "/lila"}, None))

    def test_uses_html_links_inside_tables(self):
        original = "<table>\n<tr><td>Lila</td></tr>\n</table>\n"
        expected = '<table>\n<tr><td><a href="/lila">Lila</a></td></tr>\n</table>\n'
        self.assertEqual(expected, autolinks.autolink_content(original, {"Lila": "/lila"}, None))

    def test_corrects_outdated_urls_but_not_code_or_manual_targets(self):
        old = "/fish/2025/09/29/fish_bandit"
        current = "/fish/2025/07/24/fish_bandit"
        content = f'<a href="{old}">Bandits</a> [Bandit]({old}) `{old}`'
        expected = f'<a href="{current}">Bandits</a> [Bandit]({current}) `{old}`'
        self.assertEqual(expected, autolinks.autolink_content(content, {"Bandit": current}, None))

    def test_skips_all_aliases_of_own_post(self):
        content = "Shadow heißt auch Schatten."
        self.assertEqual(
            content,
            autolinks.autolink_content(content, {"Shadow": "/shadow", "Schatten": "/shadow"}, {"Shadow", "Schatten"}),
        )


class GalleryTests(unittest.TestCase):
    def test_preserves_multiline_metadata_and_is_idempotent(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            images = root / "assets/images/fish/lila"
            images.mkdir(parents=True)
            (images / "one.webp").touch()
            (images / "two.webp").touch()
            metadata = root / "gallery.yml"
            metadata.write_text(
                '- path: "/assets/images/fish/lila/one.webp"\n'
                '  title: "Lila: Porträt"\n'
                "  caption: >-\n    Erste Zeile\n    zweite Zeile\n",
                encoding="utf-8",
            )
            with patch.object(gallery, "DOCS_DIR", root), patch.object(gallery, "GALLERY_YML", metadata):
                gallery.main()
                first = metadata.read_text(encoding="utf-8")
                entries = yaml.safe_load(first)
                self.assertEqual("Erste Zeile zweite Zeile", entries[0]["caption"])
                self.assertEqual(2, len(entries))
                gallery.main()
                self.assertEqual(first, metadata.read_text(encoding="utf-8"))


class ThumbnailTests(unittest.TestCase):
    def test_keeps_original_and_creates_thumbnail(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "fish.png"
            Image.new("RGBA", (600, 300), (0, 128, 255, 128)).save(source)
            original = source.read_bytes()
            self.assertTrue(thumbnails.process_source_image(source))
            self.assertEqual(original, source.read_bytes())
            with Image.open(source.with_name("fish_thumbnail.webp")) as thumbnail:
                self.assertEqual((400, 200), thumbnail.size)
                self.assertEqual("RGBA", thumbnail.mode)

    def test_failed_conversion_has_nonzero_exit(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "broken.png").write_text("Kein Bild", encoding="utf-8")
            with patch.object(thumbnails, "IMAGE_ROOT", root), contextlib.redirect_stdout(io.StringIO()):
                with self.assertRaises(SystemExit) as error:
                    thumbnails.main()
            self.assertEqual(1, error.exception.code)
            self.assertTrue((root / "broken.png").exists())

    def test_uppercase_original_does_not_schedule_duplicate_thumbnail(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            Image.new("RGB", (600, 300)).save(root / "fish.PNG")
            Image.new("RGB", (600, 300)).save(root / "fish.webp")
            with patch.object(thumbnails, "IMAGE_ROOT", root), patch.object(
                thumbnails, "create_thumbnail", wraps=thumbnails.create_thumbnail
            ) as create:
                thumbnails.main()
                self.assertEqual(1, create.call_count)


if __name__ == "__main__":
    unittest.main()
