# src/git_commands/__init__.py

from .init import init_command
from .cat_file import cat_file_command
from .hash_object import hash_object_command
from .ls_tree import ls_tree_command
from .write_tree import write_tree_command
from .commit_tree import commit_tree_command
from .clone import clone_command


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
    return commands.get(command_name)
