# src/git_commands/clone.py

import os

from dulwich import porcelain
from dulwich.repo import Repo


def clone_command(args):
    """
    Handles the 'clone' command by parsing the arguments and calling the
    'clone' function to clone a Git repository.

    Args:
        args (list): List of command-line arguments. Expected format:
                     [<repository_url>, <target_directory>]
    """
    # Check if the arguments list has exactly two elements
    if len(args) != 2:
        print("Usage: clone <repository_url> <target_directory>")
        return

    # Extract the repository URL and target directory from the arguments
    repo_url, target_dir = args

    # Call the 'clone' function with the repository URL and target directory
    clone(repo_url, target_dir)


def clone(repo_url, target_dir):
    """
    Clones a Git repository from the given URL into the specified directory.

    Args:
        repo_url (str): URL of the Git repository to clone.
        target_dir (str): Path to the directory where the repository should be cloned.

    Raises:
        Exception: If an error occurs during the cloning process.
    """
    # Check if the target directory does not exist and create it
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    try:
        # Use Dulwich's porcelain API to clone the repository
        porcelain.clone(source=repo_url, target=target_dir)
        print(f"Cloned repository into {target_dir}")
    
    # Handle any exceptions that occur during the cloning process
    except Exception as e:
        print(f"Error cloning repository: {e}")
