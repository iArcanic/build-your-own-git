# src/git_commands/init.py

import os


def init_command(args):
    git_dir = ".git"
    os.makedirs(os.path.join(git_dir, "objects"), exist_ok=True)
    os.makedirs(os.path.join(git_dir, "refs"), exist_ok=True)
    with open(os.path.join(git_dir, "HEAD"), "w") as f:
        f.write("ref: refs/heads/main\n")
    print(f"Initialized git directory at {git_dir}")
