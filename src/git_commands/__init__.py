# src/git_commands/__init__.py

from .init import init_command
from .cat_file import cat_file_command
from .hash_object import hash_object_command


commands = {
    "init": init_command,
    "cat-file": cat_file_command,
    "hash-object": hash_object_command,
}


def get_command(command_name):
    return commands.get(command_name)
