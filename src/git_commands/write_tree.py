# src/git_commands/write_tree.py

import hashlib
import os
import zlib


def write_tree_command(args):
    sha1 = write_tree(".")
    print(sha1)


def write_tree(directory, git_dir=".git"):
    entries = []

    for entry in sorted(os.listdir(directory)):
        if entry == git_dir.lstrip("./"):
            continue

        entry_path = os.path.join(directory, entry)

        if os.path.isdir(entry_path):
            sha1 = write_tree(entry_path, git_dir)
            mode = "040000"
            obj_type = "tree"
        else:
            sha1 = write_blob(entry_path, git_dir)
            mode = "100644"
            obj_type = "blob"

        entries.append(f"{mode} {entry}\0".encode() + bytes.fromhex(sha1))

    tree_content = b"".join(entries)
    store = b"tree " + str(len(tree_content)).encode() + b"\0" + tree_content
    tree_sha1 = hashlib.sha1(store).hexdigest()

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
    with open(file_path, "rb") as f:
        content = f.read()

    header = f"blob {len(content)}\0".encode()
    store = header + content

    sha1 = hashlib.sha1(store).hexdigest()

    object_dir = os.path.join(git_dir, "objects", sha1[:2])
    object_file = sha1[2:]
    object_path = os.path.join(object_dir, object_file)

    if not os.path.exists(object_dir):
        os.makedirs(object_dir)

    compressed_data = zlib.compress(store)

    with open(object_path, "wb") as f:
        f.write(compressed_data)

    return sha1
