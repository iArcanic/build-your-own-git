# src/git_commands/commit_tree.py

import hashlib
import os
import time
import zlib


def commit_tree_command(args):
    if len(args) < 4 or "-m" not in args:
        print("Usage: commit-tree <tree_sha> -m <message> [-p <parent_sha>]")
        return

    tree_sha = args[0]
    message_index = args.index("-m") + 1
    message = args[message_index]

    parent_sha = None
    if "-p" in args:
        parent_index = args.index("-p") + 1
        parent_sha = args[parent_index]

    sha1 = commit_tree(tree_sha, message, parent_sha)
    print(sha1)


def commit_tree(tree_sha, message, parent_sha=None, git_dir=".git"):
    author = "Author Name <author@example.com>"
    committer = "Committer Name <committer@example.com>"
    timestamp = int(time.time())
    author_time = f"{timestamp} +0000"

    commit_content = f"tree {tree_sha}\n"
    
    if parent_sha:
        commit_content += f"parent {parent_sha}\n"
    
    commit_content += f"author {author} {author_time}\n"
    commit_content += f"committer {committer} {author_time}\n"
    commit_content += f"\n{message}\n"

    commit_header = f"commit {len(commit_content)}\0"
    store = commit_header.encode() + commit_content.encode()
    commit_sha1 = hashlib.sha1(store).hexdigest()

    object_dir = os.path.join(git_dir, "objects", commit_sha1[:2])
    object_file = commit_sha1[2:]
    object_path = os.path.join(object_dir, object_file)

    if not os.path.exists(object_dir):
        os.makedirs(object_dir)

    compressed_data = zlib.compress(store)

    with open(object_path, "wb") as f:
        f.write(compressed_data)

    return commit_sha1
