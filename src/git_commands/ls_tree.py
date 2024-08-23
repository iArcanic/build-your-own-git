# src/git_commands/ls_tree.py

import os
import zlib


def ls_tree_command(args):
    if len(args) < 2 or args[0] != "--name-only":
        print("Usage: ls-tree --name-only <tree_sha>")
        return
    
    tree_sha = args[1]
    ls_tree(tree_sha, name_only=True)


def ls_tree(tree_sha, git_dir=".git", name_only=False):
    try:
        object_dir = os.path.join(git_dir, "objects", tree_sha[:2])
        object_file = tree_sha[2:]
        object_path = os.path.join(object_dir, object_file)

        with open(object_path, "rb") as f:
            raw = zlib.decompress(f.read())

        i = 0
        entries = []

        while i < len(raw):
            end_of_mode = raw.find(b' ', i)
            mode = raw[i:end_of_mode].decode('utf-8')
            i = end_of_mode + 1

            end_of_name = raw.find(b'\0', i)
            name = raw[i:end_of_name].decode('utf-8')
            i = end_of_name + 1

            sha1 = raw[i:i+20].hex()
            i += 20

            if mode == "040000":
                obj_type = "tree"
            else:
                obj_type = "blob"

            entries.append((mode, obj_type, sha1, name))

        entries.sort(key=lambda entry: entry[3])

        for entry in entries:
            if name_only:
                print(entry[3])
            else:
                print(f"{entry[0]} {entry[1]} {entry[2]}\t{entry[3]}")

    except FileNotFoundError:
        print(f"Error: Tree object {tree_sha} not found")
    except Exception as e:
        print(f"Error reading tree object: {e}")
        