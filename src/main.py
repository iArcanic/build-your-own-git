import sys

from git_commands import *


def main():
    command = sys.argv[1]
    if command == "init":
        init()
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
    main()