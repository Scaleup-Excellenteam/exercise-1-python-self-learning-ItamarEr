"""
This module provides functions to intertwine multiple iterables.
The 'interleave' function takes multiple iterables as arguments and returns a list of elements 
intertwined. The 'generator_interleave' function is similar, but it yields 
elements one by one instead of returning a list.
"""

def interleave(*args):
    """
    Intertwines elements of multiple iterables and returns them as a list.
    :param args: 0 or more iterables to intertwine.
    :return: A list of elements from the iterables, intertwined.
    """
    if not args:
        return []
    interleave_list = []
    iterables = [iter(arg) for arg in args]
    while iterables:
        for iterable in iterables:
            try:
                interleave_list.append(next(iterable))
            except StopIteration:
                iterables.remove(iterable)
    return interleave_list


def generator_interleave(*args):
    """
    Intertwines elements of multiple iterables and yields them one by one.
    :param args: 0 or more iterables to intertwine.
    :yield: Elements of the iterables, intertwined.
    """
    if not args:
        return
    iterables = [iter(arg) for arg in args]
    while iterables:
        for iterable in iterables:
            try:
                yield next(iterable)
            except StopIteration:
                iterables.remove(iterable)


if __name__ == "__main__":
    lst = interleave('abc', [1, 2, 3], ('!', '@', '#'))
    for element in lst:
        print(element)
    gen = generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))
    for element in gen:
        print(element, end=' ')
