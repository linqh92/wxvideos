# GitHub Sync Rules

## Scope

Applies to simple workflows where `main` is the only collaboration branch. This file may be copied to other project roots and reused directly.

## Core Rules

- Enter the sync flow only when the user explicitly asks to “sync to GitHub”, “commit to GitHub”, or “push to GitHub”.
- Without an explicit sync instruction, keep all changes only in the local workspace. Do NOT commit or push automatically.
- All sync operations commit and push directly to the remote `main` branch.
- Do NOT create feature branches, open Pull Requests (PRs), or perform branch-merge workflows.
- Before syncing, obtain explicit user confirmation for both the exact changes and the proposed commit message.

## Workflow

1. Confirm the current checked-out branch is `main`, and identify the remote repository and its `main` branch.
2. Compare the local workspace, local `main`, and remote `origin/main`. Also check whether the remote contains new commits that must be handled first.
3. List the planned sync scope, including at minimum:
   - Added, modified, and deleted files;
   - A brief description of each change;
   - Any conflicts, untracked files, or remote differences that may affect syncing.
4. Draft a commit message based on the actual diff. It must summarize the real changes and must not use unrelated generic or fixed wording.
5. Show the user both the **update list** and the **proposed commit message**, then explicitly ask: **是否确认同步/提交？**
6. Only after explicit confirmation, commit the approved changes to local `main` and push them to `origin/main`.
7. After completion, report the commit hash, commit message, and push result.

## Cross-platform Script

The workflow may be run without an Agent by using the repository-independent Python script:

```text
python shared/scripts/sync_github.py
```

- Requirements: Python 3.9+ and Git; no third-party Python packages are needed.
- The script fetches and compares the remote, prints the exact workspace change list and proposed commit message, and requires the user to type `同步` before it commits or pushes.
- Use `--dry-run` for a read-only preview. Use `--message "..."` to supply the proposed commit message while retaining the final interactive confirmation.
- The script stops instead of automatically merging or rebasing when the remote branch is ahead, a conflict exists, the current branch is wrong, or files change after confirmation.
- It defaults to `origin/main`. `--repo`, `--remote`, and `--branch` make the script reusable in another Git repository.

## Exception Handling

- If remote `main` contains commits missing locally, explain the difference and recommended handling first. Do not commit or push without user confirmation.
- If conflicts exist, or if some files cannot be safely judged as in-scope, list the issues and wait for the user to decide.
- The confirmed scope is exactly the update list shown to the user. If the scope changes, show the revised list and request confirmation again.
