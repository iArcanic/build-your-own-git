# src/git_commands/commit_tree.py

import hashlib
import os
import time
import zlib


def commit_tree_command(args):
    """
    Handles the 'commit-tree' command by parsing the arguments and calling
    the 'commit_tree' function to create a commit object.

    Args:
        args (list): List of command-line arguments. Expected format:
                     [<tree_sha>, -m <message> [-p <parent_sha>]]
    """
    # Validate the arguments list and ensure correct usage
    if len(args) < 4 or "-m" not in args:
        print("Usage: commit-tree <tree_sha> -m <message> [-p <parent_sha>]")
        return

    # Extract the tree SHA from the arguments
    tree_sha = args[0]

    # Find the index of the message argument and extract the message
    message_index = args.index("-m") + 1
    message = args[message_index]

    # Extract the parent SHA if provided
    parent_sha = None
    if "-p" in args:
        parent_index = args.index("-p") + 1
        parent_sha = args[parent_index]

    # Call the 'commit_tree' function to create the commit object and print its SHA
    sha1 = commit_tree(tree_sha, message, parent_sha)
    print(sha1)


def commit_tree(tree_sha, message, parent_sha=None, git_dir=".git"):
    """
    Creates a commit object from the given tree SHA and message, with an optional parent commit SHA.

    Args:
        tree_sha (str): SHA of the tree object.
        message (str): Commit message.
        parent_sha (str, optional): SHA of the parent commit object. Defaults to None.
        git_dir (str, optional): Path to the Git directory. Defaults to ".git".

    Returns:
        str: SHA1 hash of the created commit object.
    """
    # Define author and committer details
    author = "Author Name <author@example.com>"
    committer = "Committer Name <committer@example.com>"

    # Get the current timestamp and format it
    timestamp = int(time.time())
    author_time = f"{timestamp} +0000"
    
    # Build the commit content
    commit_content = f"tree {tree_sha}\n"
    if parent_sha:
        commit_content += f"parent {parent_sha}\n"
    commit_content += f"author {author} {author_time}\n"
    commit_content += f"committer {committer} {author_time}\n"
    commit_content += f"\n{message}\n"

    # Build the commit header and full commit data
    commit_header = f"commit {len(commit_content)}\0"
    store = commit_header.encode() + commit_content.encode()

    # Compute the SHA1 hash of the commit data
    commit_sha1 = hashlib.sha1(store).hexdigest()

    # Define the path to store the commit object
    object_dir = os.path.join(git_dir, "objects", commit_sha1[:2])
    object_file = commit_sha1[2:]
    object_path = os.path.join(object_dir, object_file)

    # Ensure the directory exists
    if not os.path.exists(object_dir):
        os.makedirs(object_dir)

    # Compress the commit data and write it to the file
    compressed_data = zlib.compress(store)
    with open(object_path, "wb") as f:
        f.write(compressed_data)

    return commit_sha1
