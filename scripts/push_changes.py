import subprocess
import sys
import argparse
from typing import Optional


def run(cmd: str) -> Optional[str]:
    print(f"[RUN] {cmd}")
    result = subprocess.run(
        cmd, shell=True, capture_output=True, text=True,
        encoding="utf-8", errors="replace",
    )
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    if result.returncode != 0:
        print(f"[FAIL] 命令执行失败，退出码: {result.returncode}")
        sys.exit(result.returncode)
    return result.stdout


def check_changed() -> bool:
    output = run("git status --porcelain")
    if output and output.strip():
        return True
    print("[INFO] 没有需要提交的改动，跳过。")
    return False


def push(branch: str, message: str, dry_run: bool) -> None:
    if not check_changed():
        return

    run("git add -A")

    if dry_run:
        print("[DRY RUN] 将提交信息:", message)
        print("[DRY RUN] 将推送到 origin/" + branch)
        return

    run(f'git commit -m "{message}"')
    run(f"git push origin {branch}")


def main():
    parser = argparse.ArgumentParser(description="提交并推送当前修改到 origin")
    parser.add_argument(
        "-m", "--message", default="提交当前修改",
        help="提交信息，默认: '提交当前修改'",
    )
    parser.add_argument(
        "-b", "--branch", default="main",
        help="推送的目标分支，默认: main",
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="预览模式，不实际提交和推送",
    )
    args = parser.parse_args()

    push(args.branch, args.message, args.dry_run)


if __name__ == "__main__":
    main()