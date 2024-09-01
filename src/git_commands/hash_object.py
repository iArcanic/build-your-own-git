# src/git_commands/hash_object.py

import hashlib
import os
import zlib


def hash_object_command(args):
    """
    Handles the 'hash-object' command by parsing the arguments and calling
    the 'compute_and_store_hash' function to compute and optionally store the hash.

    Args:
        args (list): List of command-line arguments. Expected format:
                     [-w <file>]
    """
    # Validate the arguments list and ensure correct usage
    if len(args) < 2 or args[0] != "-w":
        print("Usage: hash-object -w <file>")
        return
    
    # Extract the file path from arguments
    file_path = args[1]

    # Compute the hash and write the object if '-w' is specified
    compute_and_store_hash(file_path, write=True)


def compute_and_store_hash(file_path, git_dir=".git", write=False):
    """
    Computes the hash of the given file and optionally stores it in the Git directory.

    Args:
        file_path (str): Path to the file to be hashed.
        git_dir (str, optional): Path to the Git directory. Defaults to ".git".
        write (bool, optional): Whether to write the object to the Git directory. Defaults to False.
    """
    try:
        # Read the content of the file
        with open(file_path, "rb") as f:
            content = f.read()

        # Prepare the object header and concatenate with file content
        header = f"blob {len(content)}\0".encode()
        store = header + content

        # Compute the SHA1 hash of the combined header and content
        sha1 = hashlib.sha1(store).hexdigest()

        # If write flag is set, store the object in the Git directory
        if write:
            object_dir = os.path.join(git_dir, "objects", sha1[:2])
            object_file = sha1[2:]
            object_path = os.path.join(object_dir, object_file)

            # Ensure the directory exists
            if not os.path.exists(object_dir):
                os.makedirs(object_dir)

            # Compress the object data
            compressed_data = zlib.compress(store)

            # Write the compressed data to the object file
            with open(object_path, "wb") as f:
                f.write(compressed_data)

        print(sha1)

    # Handle the case where the object file does not exist
    except FileNotFoundError:
        print(f"Error: File {file_path} not found")
    
    # Handle any other exceptions that occur
    except Exception as e:
        print(f"Error hashing object: {e}")
