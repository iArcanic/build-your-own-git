# src/git_commands/cat_file.py

import os
import zlib


def cat_file_command(args):
    """
    Handles the 'cat-file' command by parsing the arguments and calling the
    'cat_file' function to display the content of a Git object.

    Args:
        args (list): List of command-line arguments. Expected format:
                     ['-p', <blob_sha>]
    """
    # Check if the arguments meet the expected format
    if len(args) < 2 or args[0] != "-p":
        print("Error: Invalid arguments for cat-file")
        return

    # Extract the SHA of the blob from the arguments
    blob_sha = args[1]

    # Call the 'cat_file' function with the blob SHA
    cat_file(blob_sha)


def cat_file(blob_sha, git_dir=".git"):
    """
    Retrieves and prints the content of a Git object based on its SHA.

    Args:
        blob_sha (str): SHA-1 hash of the Git object to retrieve.
        git_dir (str): Path to the Git directory. Defaults to ".git".
    """
    # Derive the directory and file names for the object
    object_dir = blob_sha[:2]
    object_file = blob_sha[2:]
    object_path = os.path.join(git_dir, "objects", object_dir, object_file)

    try:
        # Open and read the object file
        with open(object_path, "rb") as f:

            # Decompress the object content
            raw = zlib.decompress(f.read())

            # Split the content into header and body
            header, content = raw.split(b"\0", maxsplit=1)

            # Print the content in a decoded format
            print(content.decode("utf-8"), end="")

    # Handle the case where the object file does not exist
    except FileNotFoundError:
        print(f"Error: Object {blob_sha} not found")

    # Handle any other exceptions that occur
    except Exception as e:
        print(f"Error reading blob: {e}")
