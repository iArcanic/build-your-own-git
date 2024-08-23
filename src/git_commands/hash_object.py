# src/git_commands/hash_object.py

import hashlib
import os
import zlib


def hash_object_command(args):
    if len(args) < 2 or args[0] != "-w":
        print("Usage: hash-object -w <file>")
        return
    
    file_path = args[1]
    compute_and_store_hash(file_path, write=True)


def compute_and_store_hash(file_path, git_dir=".git", write=False):
    try:
        with open(file_path, "rb") as f:
            content = f.read()

        header = f"blob {len(content)}\0".encode()
        store = header + content

        sha1 = hashlib.sha1(store).hexdigest()

        if write:
            object_dir = os.path.join(git_dir, "objects", sha1[:2])
            object_file = sha1[2:]
            object_path = os.path.join(object_dir, object_file)

            if not os.path.exists(object_dir):
                os.makedirs(object_dir)

            compressed_data = zlib.compress(store)

            with open(object_path, "wb") as f:
                f.write(compressed_data)

        print(sha1)

    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
    except Exception as e:
        print(f"Error hashing object: {e}")
