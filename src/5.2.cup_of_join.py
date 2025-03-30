def join(*args, sep="-") -> list:
    """
    :param args: one or more lists
    :param sep: separator character, default is "-"
    :return: the lists joined together with the separator
    """
    if not args:
        return []
    joined_list = []

    for i in range(len(args)):
        for item in args[i]:
            joined_list.append(item)
        if i < len(args) - 1:
            joined_list.append(sep)

    return joined_list


if __name__ == "__main__":
    print(join([1, 2], [8], [9, 5, 6], sep='@'))
