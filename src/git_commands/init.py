# src/git_commands/init.py

import os


def init_command(args):
    """
    Initializes a new Git repository structure in the current directory.

    Args:
        args (list): List of command-line arguments. Not used in this function.
    """
    # Define the path to the Git directory
    git_dir = ".git"

    # Create the necessary directories within the Git repository
    os.makedirs(os.path.join(git_dir, "objects"), exist_ok=True)    # Directory to store Git objects
    os.makedirs(os.path.join(git_dir, "refs"), exist_ok=True)       # Directory to store references (branches/tags)

    # Create and write to the HEAD file to set the default branch reference
    with open(os.path.join(git_dir, "HEAD"), "w") as f:
        f.write("ref: refs/heads/main\n") # Points to the main branch by default

    print(f"Initialized git directory at {git_dir}")
