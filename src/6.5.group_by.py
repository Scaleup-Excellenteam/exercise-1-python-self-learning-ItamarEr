def group_by(f,iterable:iter) -> dict:
    """
    :param f: a function that takes an element of iterable and returns a key.
    :param iterable: an iterable.
    :return: a dictionary with keys as the result of f and values as the elements of iterable.
    """
    dictionary = {}
    for element in iterable:
        try:
            key = f(element)
            if key in dictionary:
                dictionary[key].append(element)
            else:
                dictionary[key] = [element]
        except Exception as e:     # catch all exceptions: ValueError, TypeError, etc.
            print(f"Error {e}")
            exit(1)
    return dictionary

if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
