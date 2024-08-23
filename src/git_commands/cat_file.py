# src/git_commands/cat_file.py

import os
import zlib


def cat_file_command(args):
    if len(args) < 2 or args[0] != "-p":
        print("Error: Invalid arguments for cat-file")
        return

    blob_sha = args[1]
    cat_file(blob_sha)


def cat_file(blob_sha, git_dir=".git"):
    object_dir = blob_sha[:2]
    object_file = blob_sha[2:]
    object_path = os.path.join(git_dir, "objects", object_dir, object_file)

    try:
        with open(object_path, "rb") as f:
            raw = zlib.decompress(f.read())
            header, content = raw.split(b"\0", maxsplit=1)
            print(content.decode("utf-8"), end="")
    except FileNotFoundError:
        print(f"Error: Object {blob_sha} not found")
    except Exception as e:
        print(f"Error reading blob: {e}")
