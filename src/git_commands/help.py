# src/git_commands/help.py

def help_command(args):
    """
    Shows an informative help message.

    Args:
        args (list): List of command-line arguments. Not used in this function.
    """
    help_text = """
Available commands:
  init                                                  - Initialize a new Git repository.
  hash-object -w <file>                                 - Compute and store the hash of a file.
  cat-file -p <sha>                                     - Print the contents of a blob object.
  ls-tree --name-only <tree_sha>                        - List the contents of a tree object.
  write-tree                                            - Write the current directory structure to a tree object.
  commit-tree <tree_sha> -m <message> [-p <parent_sha>] - Create a new commit object.
  clone <repo_url> <target_dir>                         - Clone a Git repository.
  help                                                  - Show this help message.
    """
    print(help_text)
