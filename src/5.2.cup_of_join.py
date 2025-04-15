"""
This module provides a function to join multiple lists together, 
optionally inserting a separator between them.
"""

def cup_of_join(*args, sep=None) -> list:
    """
    Joins multiple lists together, optionally inserting a separator between them.

    :param args: One or more lists.
    :param sep: Separator character (default is None).
    :return: A single list containing all elements from the input lists, 
             with the separator inserted between lists if provided.
    """
    joined_list = []
    for _, lst in enumerate(args):
        joined_list.extend(lst)
        if sep is not None:
            joined_list.append(sep)

    return joined_list


if __name__ == "__main__":
    print(cup_of_join([1, 2], ['a'], [True, False], sep='-'))
