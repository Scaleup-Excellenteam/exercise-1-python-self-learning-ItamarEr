"""
This module provides functions to intertwine multiple iterables.
The 'interleave' function takes multiple iterables as arguments and returns a list of elements
intertwined. The 'generator_interleave' function is similar, but it yields
elements one by one instead of returning a list.
"""
from itertools import zip_longest


def interleave(*args):
    """
    Intertwines elements of multiple iterables and returns them as a list.
    :param args: 0 or more iterables to intertwine.
    :return: A list of elements from the iterables, intertwined.
    """
    return [element for elements in zip_longest(*args) for element in elements if element is not None]


def generator_interleave(*args):
    """
    Intertwines elements of multiple iterables and yields them one by one.
    :param args: 0 or more iterables to intertwine.
    :yield: Elements of the iterables, intertwined.
    """
    yield from (element for elements in zip_longest(*args) for element in elements if element is not None)


def main():
    lst = interleave('abc', [1, 2, 3], ('!', '@', '#'))
    for element in lst:
        print(element, end=' ')
    print()
    gen = generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))
    for element in gen:
        print(element, end=' ')


if __name__ == "__main__":
    main()
