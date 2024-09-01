# src/main.py

import sys

from git_commands import get_command


def main():
    # Check if at least an argument is provided
    if len(sys.argv) < 2:
        print("Error: No command provided")
        return

    # First argument is the command
    command = sys.argv[1]

    # Get the corresponding command from the argument
    command_func = get_command(command)

    # Check if the command exists
    if command_func:
        try:
            # Call the corresponding command and pass subsequent arguments
            command_func(sys.argv[2:])
        except Exception as e:
            # Handle any exceptions raised by that command
            print(f"Error executing command '{command}': {e}")
    else:
        # If the command does not exist
        print(f"Unknown command '{command}'")


if __name__ == "__main__":
    main()
