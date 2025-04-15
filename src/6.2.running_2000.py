import time


def running_2000(f,*args, **kwargs) -> float:
    """
    :param f: a function.
    :param args: 0 or more arguments to pass to f.
    :param kwargs: 0 or more keyword arguments to pass to f.
    :return: the time it took to run f.
    """
    start = time.time()
    f(*args, **kwargs)
    end = time.time()
    return (end - start) * 1000  # convert to milliseconds


def main():
    try:
        running_2000("Hi {name}".format, name="Bug")
    except TypeError as e:
        print(f"Error {e}")
        exit(1)
        

if __name__ == '__main__':
    main()
