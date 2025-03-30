def interleave(*args):
    """
    :param args: 0 or more iterables to intertwine
    :return: list of the iterables intertwined
    """
    if not args:
        return None
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
    :param args: 0 or more iterables to intertwine
    :yield: elements of the iterables intertwined
    """
    if not args:
        return None
    iterables = [iter(arg) for arg in args]
    while iterables:
        for iterable in iterables:
            try:
                yield next(iterable)
            except StopIteration:
                iterables.remove(iterable)


if __name__ == "__main__":
    list = interleave('abc', [1, 2, 3], ('!', '@', '#'))
    for element in list:
        print(element)
    gen = generator_interleave('abc', [1, 2, 3], ('!', '@', '#'))
    for element in gen:
        print(element, end=' ')
