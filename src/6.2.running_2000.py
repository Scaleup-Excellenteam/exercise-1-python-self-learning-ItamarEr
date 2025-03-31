"""
This module provides a function to measure the execution time of another function.
The `running_2000` function takes a function `f` and its arguments, executes it, and 
returns the time taken for execution. It also handles exceptions.
"""
import time
import sys


def running_2000(f, *args, **kwargs) -> float:
    """
    Measures the execution time of a given function.

    :param f: A function to be executed.
    :param args: Positional arguments to pass to `f`.
    :param kwargs: Keyword arguments to pass to `f`.
    :return: The time (in seconds) taken to run `f`.
    """
    start = time.time()
    try:
        f(*args, **kwargs)
    except TypeError:
        sys.exit("Error: Incorrect arguments passed to the function.")
    except ValueError:
        sys.exit("Error: Function encountered a value-related issue.")
    except Exception as e:  # Catch unexpected exceptions
        sys.exit(f"Unexpected error: {e}")

    end = time.time()
    return end - start


if __name__ == '__main__':
    print(running_2000(len, [1, 2, 3], [4, 5, 6]))
