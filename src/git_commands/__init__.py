# src/git_commands/__init__.py

from .init import init_command
from .cat_file import cat_file_command
from .hash_object import hash_object_command
from .ls_tree import ls_tree_command
from .write_tree import write_tree_command
from .commit_tree import commit_tree_command
from .clone import clone_command

# Dictionary mapping to command name strings to function names
commands = {
    "init": init_command,
    "cat-file": cat_file_command,
    "hash-object": hash_object_command,
    "ls-tree": ls_tree_command,
    "write-tree": write_tree_command,
    "commit-tree": commit_tree_command,
    "clone": clone_command,
}


def get_command(command_name):
    """
    Retrieves the function associated with a given command name.

    Args:
        command_name (str): The name of the command to retrieve.

    Returns:
        function: The function associated with the command name, or None if the command is not found.
    """
    return commands.get(command_name)
