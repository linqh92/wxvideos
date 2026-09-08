#!/usr/bin/env python3
"""Safely preview, commit, and push a Git repository.

The script intentionally keeps confirmation interactive. It has no third-party
dependencies and invokes Git without a shell, so it can be copied to other
repositories and used on Windows, macOS, or Linux.
"""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


CONFIRM_WORD = "同步"
CONFLICT_CODES = {"DD", "AU", "UD", "UA", "DU", "AA", "UU"}


class SyncError(RuntimeError):
    """A user-actionable synchronization error."""


@dataclass(frozen=True)
class Change:
    code: str
    path: str
    old_path: str | None = None


def _configure_console() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure:
            reconfigure(encoding="utf-8", errors="replace")


def run_git(
    repo: Path,
    args: Sequence[str],
    *,
    check: bool = True,
    text: bool = True,
) -> subprocess.CompletedProcess:
    command = ["git", "-c", "core.quotepath=false", *args]
    try:
        result = subprocess.run(
            command,
            cwd=repo,
            capture_output=True,
            text=text,
            encoding="utf-8" if text else None,
            errors="replace" if text else None,
            check=False,
        )
    except FileNotFoundError as exc:
        raise SyncError("未找到 Git。请先安装 Git，并确认 git 命令可用。") from exc
    if check and result.returncode != 0:
        stderr = result.stderr.strip() if text else result.stderr.decode("utf-8", "replace").strip()
        stdout = result.stdout.strip() if text else result.stdout.decode("utf-8", "replace").strip()
        detail = stderr or stdout or f"退出码 {result.returncode}"
        raise SyncError(f"Git 命令执行失败：{' '.join(args)}\n{detail}")
    return result


def repository_root(start: Path) -> Path:
    result = run_git(start, ["rev-parse", "--show-toplevel"])
    return Path(result.stdout.strip()).resolve()


def status_snapshot(repo: Path) -> bytes:
    result = run_git(
        repo,
        ["status", "--porcelain=v1", "-z", "--untracked-files=all"],
        text=False,
    )
    return result.stdout


def parse_status(snapshot: bytes) -> list[Change]:
    fields = snapshot.split(b"\0")
    changes: list[Change] = []
    index = 0
    while index < len(fields) and fields[index]:
        record = fields[index].decode("utf-8", "replace")
        if len(record) < 4:
            raise SyncError("无法解析 git status 输出。")
        code = record[:2]
        path = record[3:]
        old_path = None
        if "R" in code or "C" in code:
            index += 1
            if index >= len(fields) or not fields[index]:
                raise SyncError("无法解析重命名文件的 git status 输出。")
            old_path = fields[index].decode("utf-8", "replace")
        changes.append(Change(code=code, path=path, old_path=old_path))
        index += 1
    return changes


def change_label(change: Change) -> str:
    code = change.code
    if code == "??":
        return "新增"
    if code in CONFLICT_CODES or "U" in code:
        return "冲突"
    if "R" in code:
        return "重命名"
    if "C" in code:
        return "复制"
    if "D" in code:
        return "删除"
    if "A" in code:
        return "新增"
    return "修改"


def suggested_message(changes: Sequence[Change]) -> str:
    paths = [change.path.replace("\\", "/") for change in changes]
    groups: list[str] = []
    if any(path.startswith("accounts/") for path in paths):
        groups.append("账号内容")
    if any(path.startswith("shared/") for path in paths):
        groups.append("公共规则与工具")
    if any(path.startswith(".codex/") for path in paths):
        groups.append("内容生产技能")
    documentation = {"AGENTS.md", "README.md", "GitHub-Sync-Rules.md"}
    if any(path in documentation or path.startswith("docs/") for path in paths):
        groups.append("项目规则与说明")
    known = ("accounts/", "shared/", ".codex/", "docs/")
    if any(path not in documentation and not path.startswith(known) for path in paths):
        groups.append("项目文件")

    if not groups:
        groups = ["项目文件"]
    subject = "、".join(groups[:3])
    if len(groups) > 3:
        subject += "等"
    return f"更新{subject}（{len(changes)} 个文件）"


def ahead_behind(repo: Path, remote_ref: str) -> tuple[int, int]:
    output = run_git(
        repo, ["rev-list", "--left-right", "--count", f"HEAD...{remote_ref}"]
    ).stdout.strip()
    try:
        ahead_text, behind_text = output.split()
        return int(ahead_text), int(behind_text)
    except (ValueError, TypeError) as exc:
        raise SyncError(f"无法解析本地与远端的提交差异：{output}") from exc


def fetch_remote(repo: Path, remote: str, branch: str) -> str:
    url = run_git(repo, ["remote", "get-url", remote]).stdout.strip()
    run_git(repo, ["fetch", "--prune", remote, branch])
    remote_ref = f"refs/remotes/{remote}/{branch}"
    exists = run_git(repo, ["show-ref", "--verify", "--quiet", remote_ref], check=False)
    if exists.returncode != 0:
        raise SyncError(f"远端分支不存在：{remote}/{branch}")
    return url


def show_plan(
    repo: Path,
    remote: str,
    branch: str,
    remote_url: str,
    changes: Sequence[Change],
    ahead: int,
) -> None:
    print("\nGitHub 同步预览")
    print(f"仓库：{repo}")
    print(f"远端：{remote_url}")
    print(f"分支：{branch} -> {remote}/{branch}")
    print(f"本地尚未推送的提交：{ahead} 个")

    if ahead:
        commits = run_git(repo, ["log", "--oneline", f"{remote}/{branch}..HEAD"]).stdout.strip()
        print("\n尚未推送的提交：")
        print(commits)

    if changes:
        print(f"\n本次工作区变更：{len(changes)} 个文件")
        for change in changes:
            label = change_label(change)
            if change.old_path:
                print(f"  [{label}] {change.old_path} -> {change.path}")
            else:
                print(f"  [{label}] {change.path}")
        stat = run_git(repo, ["diff", "--stat", "HEAD"]).stdout.strip()
        if stat:
            print("\n变更统计：")
            print(stat)
    else:
        print("\n工作区没有待提交变更。")


def read_commit_message(proposed: str, supplied: str | None) -> str:
    if supplied is not None:
        message = supplied.strip()
        if not message:
            raise SyncError("提交信息不能为空。")
        return message
    if not sys.stdin.isatty():
        raise SyncError("当前不是交互终端。请使用 --message 提供提交信息。")
    print(f"\n建议提交信息：{proposed}")
    entered = input("按回车采用，或输入新的提交信息：").strip()
    return entered or proposed


def confirm_sync(message: str | None, change_count: int, ahead: int) -> None:
    if not sys.stdin.isatty():
        raise SyncError("当前不是交互终端，无法取得明确确认；已取消同步。")
    print("\n最终确认")
    print(f"将提交 {change_count} 个工作区文件。" if change_count else "不会创建新提交。")
    if message:
        print(f"提交信息：{message}")
    print(f"随后会把当前分支（含 {ahead} 个既有未推送提交）推送到远端。")
    answer = input(f"确认无误请输入“{CONFIRM_WORD}”，其他输入均取消：").strip()
    if answer != CONFIRM_WORD:
        raise SyncError("用户取消同步；未提交、未推送。")


def ensure_safe_state(repo: Path, branch: str, changes: Sequence[Change]) -> None:
    current = run_git(repo, ["branch", "--show-current"]).stdout.strip()
    if current != branch:
        raise SyncError(f"当前分支是 {current or '(detached HEAD)'}，必须先切换到 {branch}。")
    conflicts = [change.path for change in changes if change_label(change) == "冲突"]
    if conflicts:
        rendered = "\n".join(f"  - {path}" for path in conflicts)
        raise SyncError(f"存在未解决冲突，已停止同步：\n{rendered}")


def parse_args(argv: Sequence[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="预览、确认并安全地提交和推送 Git 变更。"
    )
    parser.add_argument("--repo", default=".", help="仓库内任意路径（默认：当前目录）")
    parser.add_argument("--remote", default="origin", help="远端名称（默认：origin）")
    parser.add_argument("--branch", default="main", help="目标分支（默认：main）")
    parser.add_argument("-m", "--message", help="提交信息；省略时交互输入")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="只获取远端状态并显示同步预览，不提交、不推送",
    )
    return parser.parse_args(argv)


def main(argv: Sequence[str] | None = None) -> int:
    _configure_console()
    args = parse_args(argv)
    try:
        start = Path(os.path.expanduser(args.repo)).resolve()
        repo = repository_root(start)
        initial_snapshot = status_snapshot(repo)
        changes = parse_status(initial_snapshot)
        ensure_safe_state(repo, args.branch, changes)

        print(f"正在检查 {args.remote}/{args.branch} ...")
        remote_url = fetch_remote(repo, args.remote, args.branch)
        ahead, behind = ahead_behind(repo, f"{args.remote}/{args.branch}")
        if behind:
            raise SyncError(
                f"远端 {args.remote}/{args.branch} 比本地多 {behind} 个提交。"
                "请先处理远端更新；脚本不会自动合并或变基。"
            )

        show_plan(repo, args.remote, args.branch, remote_url, changes, ahead)
        if not changes and ahead == 0:
            print("\n本地与远端已经一致，无需同步。")
            return 0
        if args.dry_run:
            print("\n预览完成：未提交、未推送。")
            return 0

        message = read_commit_message(suggested_message(changes), args.message) if changes else None
        confirm_sync(message, len(changes), ahead)

        if status_snapshot(repo) != initial_snapshot:
            raise SyncError("确认后工作区发生了变化。请重新运行脚本并再次确认。")

        # Fetch again to close the window in which the remote could advance while
        # the user reviewed the plan.
        fetch_remote(repo, args.remote, args.branch)
        _, behind = ahead_behind(repo, f"{args.remote}/{args.branch}")
        if behind:
            raise SyncError("确认期间远端出现了新提交。请处理远端更新后重新运行。")

        if changes:
            run_git(repo, ["add", "--all"])
            staged = run_git(repo, ["diff", "--cached", "--name-only", "-z"], text=False).stdout
            if not staged:
                raise SyncError("暂存后没有可提交的变更；已停止。")
            commit = run_git(repo, ["commit", "-m", message], check=False)
            if commit.returncode != 0:
                detail = commit.stderr.strip() or commit.stdout.strip()
                raise SyncError(f"提交失败，变更仍保留在本地：\n{detail}")

        push = run_git(
            repo,
            ["push", args.remote, f"{args.branch}:{args.branch}"],
            check=False,
        )
        if push.returncode != 0:
            detail = push.stderr.strip() or push.stdout.strip()
            raise SyncError(f"推送失败；本地提交已保留，可排查后重试：\n{detail}")

        commit_hash = run_git(repo, ["rev-parse", "--short", "HEAD"]).stdout.strip()
        final_message = run_git(repo, ["log", "-1", "--pretty=%s"]).stdout.strip()
        print("\n同步完成")
        print(f"提交：{commit_hash}")
        print(f"信息：{final_message}")
        print(f"推送：{args.remote}/{args.branch} 成功")
        return 0
    except SyncError as exc:
        print(f"\n同步已停止：{exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
