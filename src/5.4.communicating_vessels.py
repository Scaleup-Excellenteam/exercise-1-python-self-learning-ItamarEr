
def communicating_vessels(*args):
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
    gen = communicating_vessels('abc', [1, 2, 3], ('!', '@', '#'))
    for element in gen:
        print(element, end=' ')