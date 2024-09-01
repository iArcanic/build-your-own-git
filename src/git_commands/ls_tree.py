# src/git_commands/ls_tree.py

import os
import zlib


def ls_tree_command(args):
    """
    Command-line interface for listing the contents of a tree object.

    Args:
        args (list): Command-line arguments. Expected to include the '--name-only' flag and tree SHA.
    """
    # Check if the arguments meet the expected format
    if len(args) < 2 or args[0] != "--name-only":
        print("Usage: ls-tree --name-only <tree_sha>")
        return
    
    # Extract the tree SHA from the arguments
    tree_sha = args[1]

    # Call the 'ls_file' function with the tree SHA
    ls_tree(tree_sha, name_only=True)


def ls_tree(tree_sha, git_dir=".git", name_only=False):
    """
    Lists the contents of a tree object.

    Args:
        tree_sha (str): SHA of the tree object to be listed.
        git_dir (str): Directory where the Git objects are stored. Defaults to '.git'.
        name_only (bool): If True, only print the names of the entries. Defaults to False.
    """
    try:
        # Construct the path to the tree object file
        object_dir = os.path.join(git_dir, "objects", tree_sha[:2])
        object_file = tree_sha[2:]
        object_path = os.path.join(object_dir, object_file)

        # Read and decompress the tree object data
        with open(object_path, "rb") as f:
            raw = zlib.decompress(f.read())

        i = 0
        entries = []

        # Parse the tree object data
        while i < len(raw):
            # Extract the mode of the entry (e.g., '040000' for tree, '100644' for blob)
            end_of_mode = raw.find(b' ', i)
            mode = raw[i:end_of_mode].decode('utf-8')
            i = end_of_mode + 1

            # Extract the name of the entry
            end_of_name = raw.find(b'\0', i)
            name = raw[i:end_of_name].decode('utf-8')
            i = end_of_name + 1

            # Extract the SHA1 hash of the entry
            sha1 = raw[i:i+20].hex()
            i += 20

            # Determine the type of object (tree or blob)
            obj_type = "tree" if mode == "040000" else "blob"

            # Append the entry to the list
            entries.append((mode, obj_type, sha1, name))
        
        # Sort entries by name
        entries.sort(key=lambda entry: entry[3])

        # Print entries based on the 'name_only' flag
        for entry in entries:
            if name_only:
                print(entry[3])
            else:
                print(f"{entry[0]} {entry[1]} {entry[2]}\t{entry[3]}")

    # Handle the case where the tree SHA does not exist
    except FileNotFoundError:
        print(f"Error: Tree object {tree_sha} not found")

    # Handle any other exceptions that occur
    except Exception as e:
        print(f"Error reading tree object: {e}")
        