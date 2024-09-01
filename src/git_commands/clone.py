# src/git_commands/clone.py

import os

from dulwich import porcelain
from dulwich.repo import Repo


def clone_command(args):
    if len(args) != 2:
        print("Usage: clone <repository_url> <target_directory>")
        return

    repo_url, target_dir = args
    clone(repo_url, target_dir)


def clone(repo_url, target_dir):
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    try:
        porcelain.clone(source=repo_url, target=target_dir)
        print(f"Cloned repository into {target_dir}")
    except Exception as e:
        print(f"Error cloning repository: {e}")
