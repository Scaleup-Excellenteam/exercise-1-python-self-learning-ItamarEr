import time


def running_2000(f,*args, **kwargs) -> float:
    """
    :param f: a function.
    :param args: 0 or more arguments to pass to f.
    :param kwargs: 0 or more keyword arguments to pass to f.
    :return: the time it took to run f.
    """
    start = time.time()
    try:
        f(*args, **kwargs)
    except Exception as e:    # catch all exceptions: ValueError, TypeError, etc.
        print(f"Error: {e}")
        exit(1)
    end = time.time()
    return end - start



if __name__ == '__main__':
    print(running_2000(len, [1, 2, 3], [4, 5, 6]))
    
