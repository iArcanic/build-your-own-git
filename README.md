# build-your-own-git

![Python Version](https://img.shields.io/badge/Python-3.x-blue.svg)

Part of [CodeCrafter's Build your Own Git Challenge](app.codecrafters.io/courses/git/introduction).

## 1 TL;DR / Quickstart

```bash
pip3 install -r requirements.txt
```

```bash
python3 main.py <git_command>
```

For a list of valid commands and their usage or use:

```bash
python3 main.py help
```

Alternatively, see [`src/git_commands`](https://github.com/iArcanic/build-your-own-git/tree/main/src/git_commands).

## 2 Features

This project implements a basic version control system, akin to that of Git, using Python. It supports several core Git commands, allowing users to simulate and interact with repositories in the following ways:

- **Initialise a repository** ([`git init`](https://github.com/iArcanic/build-your-own-git/blob/main/src/git_commands/init.py)): Set up a new Git repository.
- **Hash objects** ([`git hash-object`](https://github.com/iArcanic/build-your-own-git/blob/main/src/git_commands/hash_object.py)): Compute the SHA-1 hash of a file's contents and optionally store the file as a Git object.
- **View file content** ([`git cat-file`](https://github.com/iArcanic/build-your-own-git/blob/main/src/git_commands/cat_file.py)): Display the contents of a blob object.
- **List directory tree** ([`git ls-tree`](https://github.com/iArcanic/build-your-own-git/blob/main/src/git_commands/ls_tree.py)): List the contents of a tree object.
- **Write tree**: ([`git write-tree`](https://github.com/iArcanic/build-your-own-git/blob/main/src/git_commands/write_tree.py)): Write the current directory structure to tree object.
- **Commit tree** ([`git commit-tree`](https://github.com/iArcanic/build-your-own-git/blob/main/src/git_commands/commit_tree.py)): Create a new commit object from a tree and optionally a parent commit.
- **Clone remote repositories** ([`git clone`](https://github.com/iArcanic/build-your-own-git/blob/main/src/git_commands/clone.py)): Clone a Git repository from a remote URL.

These commands are implemented to closely mimic the functionality of their counterparts in Git. It is a simplified yet effective educational tool for understanding how Git works under the hood.

## 3 Prerequisites

Before you can run or test this project, ensure that you have the following installed on your system.

### 3.1 Python 3.x

This project is built using Python 3.x. Ensure that you have a valid version of Python 3.x installed on your system.

You can download and install the Python 3.x distribution from the [official Python website](https://www.python.org/downloads/).

> [!NOTE]
> Older versions may work but Python 3.6+ is recommended.

## 4 Usage

1. Clone this repository to your local machine

```bash
git clone https://github.com/iArcanic/build-your-own-git.git
```

2. Navigate to the project's root directory.

```bash
cd build-your-own-git
```

3. Install the required Python dependencies.

```bash
pip3 install -r requirements.txt
```

4. Navigate to the project's source directory.

```bash
cd src
```

5. Run the main Python script with a valid Git command (use `python3 main.py help` for a list of valid commands and their usage).

```bash
python3 main.py <git_command>
```

## 5 Acknowledgements

- [CodeCrafter's Build your Own Git Challenge](app.codecrafters.io/courses/git/introduction)
