from __future__ import annotations

import importlib.util
import io
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch


SCRIPT_PATH = Path(__file__).with_name("sync_github.py")
SPEC = importlib.util.spec_from_file_location("sync_github", SCRIPT_PATH)
sync_github = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = sync_github
SPEC.loader.exec_module(sync_github)


def git(cwd: Path, *args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["git", "-c", "core.quotepath=false", *args],
        cwd=cwd,
        text=True,
        encoding="utf-8",
        capture_output=True,
        check=True,
    )


class SyncGithubTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.remote = root / "remote.git"
        self.repo = root / "repo"
        git(root, "init", "--bare", str(self.remote))
        git(root, "init", "-b", "main", str(self.repo))
        git(self.repo, "config", "user.name", "Test User")
        git(self.repo, "config", "user.email", "test@example.com")
        git(self.repo, "remote", "add", "origin", str(self.remote))
        (self.repo / "README.md").write_text("initial\n", encoding="utf-8")
        git(self.repo, "add", "README.md")
        git(self.repo, "commit", "-m", "initial")
        git(self.repo, "push", "-u", "origin", "main")

    def tearDown(self) -> None:
        self.temp.cleanup()

    def test_parse_status_and_message(self) -> None:
        snapshot = b" M README.md\0?? shared/scripts/new.py\0"
        changes = sync_github.parse_status(snapshot)
        self.assertEqual(["修改", "新增"], [sync_github.change_label(c) for c in changes])
        self.assertIn("公共规则与工具", sync_github.suggested_message(changes))

    def test_dry_run_does_not_commit(self) -> None:
        (self.repo / "README.md").write_text("changed\n", encoding="utf-8")
        before = git(self.repo, "rev-parse", "HEAD").stdout.strip()
        result = subprocess.run(
            [sys.executable, str(SCRIPT_PATH), "--repo", str(self.repo), "--dry-run"],
            text=True,
            encoding="utf-8",
            capture_output=True,
            check=False,
        )
        self.assertEqual(0, result.returncode, result.stderr)
        self.assertIn("预览完成", result.stdout)
        self.assertEqual(before, git(self.repo, "rev-parse", "HEAD").stdout.strip())

    def test_confirmed_sync_commits_and_pushes(self) -> None:
        (self.repo / "README.md").rename(self.repo / "说明.md")

        class InteractiveInput(io.StringIO):
            def isatty(self) -> bool:
                return True

        stdout = io.StringIO()
        stderr = io.StringIO()
        with (
            patch.object(sys, "stdin", InteractiveInput("同步\n")),
            redirect_stdout(stdout),
            redirect_stderr(stderr),
        ):
            result = sync_github.main(
                ["--repo", str(self.repo), "--message", "更新测试文件"]
            )

        self.assertEqual(0, result, stderr.getvalue())
        self.assertIn("同步完成", stdout.getvalue())
        remote_subject = git(
            self.repo, "log", "-1", "--pretty=%s", "origin/main"
        ).stdout.strip()
        self.assertEqual("更新测试文件", remote_subject)
        remote_files = git(self.repo, "ls-tree", "-r", "--name-only", "origin/main").stdout
        self.assertIn("说明.md", remote_files)


if __name__ == "__main__":
    unittest.main()
