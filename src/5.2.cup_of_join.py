def cup_of_join(*args, sep=None) -> list:
    """
    :param args: one or more lists
    :param sep: separator character, default is None
    :return: the lists joined together with the separator
    """
    if not args:
        return []
    joined_list = []

    for i in range(len(args)):
        for item in args[i]:
            joined_list.append(item)
        if sep is not None:
            joined_list.append(sep)

    return joined_list


if __name__ == "__main__":
    print(cup_of_join([1, 2], ['a'], [True, False], sep='-'))
