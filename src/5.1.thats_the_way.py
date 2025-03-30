import os


def thats_the_way(path: str) -> list:
    """
    :param path: path to a directory
    :return: list of files in the directory that start with "deep".
    """
    if not os.path.exists(path):
        return []                # path does not exist
    if not os.path.isdir(path):
        return []               # path is not a directory
    all_files = os.listdir(path)
    return [file for file in all_files if file.startswith("deep")]



if __name__ == "__main__":
    deep_files = thats_the_way(os.getcwd())
    print(deep_files)
