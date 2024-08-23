# src/main.py

import sys

from git_commands import get_command


def main():
    if len(sys.argv) < 2:
        print("Error: No command provided")
        return

    command = sys.argv[1]
    command_func = get_command(command)

    if command_func:
        try:
            command_func(sys.argv[2:])
        except Exception as e:
            print(f"Error executing command '{command}': {e}")
    else:
        print(f"Unknown command '{command}'")


if __name__ == "__main__":
    main()
