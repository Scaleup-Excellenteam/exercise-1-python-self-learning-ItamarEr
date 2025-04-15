"""
This module provides a function to list files in a directory that start with "deep".
"""
import os


def thats_the_way(path: str) -> list:
    """
    :param path: path to a directory
    :return: list of files in the directory that start with "deep".
    """
    try:
        all_files = os.listdir(path)
        return [file for file in all_files if file.startswith("deep")]
    except (FileNotFoundError, NotADirectoryError):
        return []  # Return an empty list if the path is invalid or not a directory


def main():
    deep_files = thats_the_way(os.getcwd())
    print(deep_files)

if __name__ == "__main__":
    main()
