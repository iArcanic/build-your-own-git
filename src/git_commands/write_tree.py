# src/git_commands/write_tree.py

import hashlib
import os
import zlib


def write_tree_command(args):
    """
    Command-line interface for writing a tree object.

    Args:
        args (list): Command-line arguments. Currently, this function does not use any arguments.
    """
    sha1 = write_tree(".")
    print(sha1)


def write_tree(directory, git_dir=".git"):
    """
    Recursively writes a tree object for the contents of a directory.

    Args:
        directory (str): The directory to be written as a tree object.
        git_dir (str): Directory where the Git objects are stored. Defaults to '.git'.
    
    Returns:
        str: The SHA1 hash of the created tree object.
    """
    entries = []

    # Iterate through the directory contents
    for entry in sorted(os.listdir(directory)):
        if entry == git_dir.lstrip("./"):
            continue

        entry_path = os.path.join(directory, entry)

        if os.path.isdir(entry_path):
            # Recursively write subdirectories as tree objects
            sha1 = write_tree(entry_path, git_dir)
            mode = "040000"
            obj_type = "tree"
        else:
            # Write files as blob objects
            sha1 = write_blob(entry_path, git_dir)
            mode = "100644"
            obj_type = "blob"

        # Append the mode, name, and SHA1 to the entries list
        entries.append(f"{mode} {entry}\0".encode() + bytes.fromhex(sha1))

    # Construct the tree object content
    tree_content = b"".join(entries)
    store = b"tree " + str(len(tree_content)).encode() + b"\0" + tree_content
    tree_sha1 = hashlib.sha1(store).hexdigest()

    # Save the tree object to the .git/objects directory
    object_dir = os.path.join(git_dir, "objects", tree_sha1[:2])
    object_file = tree_sha1[2:]
    object_path = os.path.join(object_dir, object_file)

    if not os.path.exists(object_dir):
        os.makedirs(object_dir)

    compressed_data = zlib.compress(store)

    with open(object_path, "wb") as f:
        f.write(compressed_data)

    return tree_sha1


def write_blob(file_path, git_dir=".git"):
    """
    Writes a blob object for a file.

    Args:
        file_path (str): The path to the file to be written as a blob object.
        git_dir (str): Directory where the Git objects are stored. Defaults to '.git'.
    
    Returns:
        str: The SHA1 hash of the created blob object.
    """
    with open(file_path, "rb") as f:
        content = f.read()

    # Construct the blob object content
    header = f"blob {len(content)}\0".encode()
    store = header + content

    sha1 = hashlib.sha1(store).hexdigest()

    # Save the blob object to the .git/objects directory
    object_dir = os.path.join(git_dir, "objects", sha1[:2])
    object_file = sha1[2:]
    object_path = os.path.join(object_dir, object_file)

    if not os.path.exists(object_dir):
        os.makedirs(object_dir)

    compressed_data = zlib.compress(store)

    with open(object_path, "wb") as f:
        f.write(compressed_data)

    return sha1
