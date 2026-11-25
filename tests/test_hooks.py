import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PushHookTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        (self.root / "scripts").mkdir()
        (self.root / "docs").mkdir()
        for name in ("pre_push.sh", "check_generated.sh"):
            shutil.copyfile(ROOT / "scripts" / name, self.root / "scripts" / name)
        self.git("init", "--quiet")
        self.git("add", ".")
        self.git("-c", "user.name=Test", "-c", "user.email=test@example.invalid",
                 "-c", "commit.gpgsign=false", "-c", "core.hooksPath=/dev/null",
                 "commit", "--quiet", "-m", "test: Ausgangszustand")
        tools = self.root / ".git/test-tools"
        tools.mkdir()
        npm = tools / "npm"
        npm.write_text(
            '#!/bin/bash\nset -euo pipefail\nprintf "%s\\n" "$*" >> .git/commands\n'
            'if [[ "$*" == "run content:check" ]]; then\n'
            '  if [[ "${GENERATE_CHANGE:-}" == 1 ]]; then echo neu > docs/generated.md; fi\n'
            '  bash scripts/check_generated.sh\n'
            'fi\nif [[ "$*" == "run check" ]]; then exit "${CHECK_RESULT:-0}"; fi\n',
            encoding="utf-8",
        )
        npm.chmod(0o755)
        self.env = {**os.environ, "PATH": f"{tools}:{os.environ['PATH']}"}

    def git(self, *args):
        return subprocess.run(["git", *args], cwd=self.root, check=True, capture_output=True, text=True)

    def run_hook(self, **env):
        return subprocess.run(["bash", "scripts/pre_push.sh"], cwd=self.root,
                              env={**self.env, **env}, capture_output=True, text=True)

    def test_clean_push_runs_generation_and_checks(self):
        self.assertEqual(0, self.run_hook().returncode)
        self.assertEqual("run content:check\nrun check\n", (self.root / ".git/commands").read_text())

    def test_uncommitted_work_is_not_modified(self):
        pending = self.root / "pending.txt"
        pending.write_text("unverändert")
        self.assertNotEqual(0, self.run_hook().returncode)
        self.assertEqual("unverändert", pending.read_text())
        self.assertFalse((self.root / ".git/commands").exists())

    def test_generated_files_abort_push_without_committing(self):
        before = self.git("rev-parse", "HEAD").stdout
        result = self.run_hook(GENERATE_CHANGE="1")
        self.assertNotEqual(0, result.returncode)
        self.assertIn("committen", result.stderr)
        self.assertEqual(before, self.git("rev-parse", "HEAD").stdout)
        self.assertTrue((self.root / "docs/generated.md").exists())
        self.assertEqual("run content:check\n", (self.root / ".git/commands").read_text())

    def test_failed_checks_block_push(self):
        self.assertNotEqual(0, self.run_hook(CHECK_RESULT="1").returncode)
