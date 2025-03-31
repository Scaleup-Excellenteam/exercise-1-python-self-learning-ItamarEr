"""
This module provides a function to group elements of an iterable based on a given function.
The 'group_by' function applies a function 'f' to each element in the iterable and groups 
the elements by the returned key. The result is a dictionary where the keys are computed 
by 'f', and the values are lists of elements that share the same key.
"""
import sys


def group_by(f, iterable: iter) -> dict:
    """
    Groups elements of an iterable based on the key returned by function `f`.
    :param f: A function that takes an element of `iterable` and returns a key.
    :param iterable: An iterable containing elements to be grouped.
    :return: A dictionary where keys are results of `f(element)`, and values are lists 
             of elements from `iterable` that share the same key.
    """
    dictionary = {}
    for element in iterable:
        try:
            key = f(element)
            if key in dictionary:
                dictionary[key].append(element)
            else:
                dictionary[key] = [element]
        except TypeError:
            print(f"Error: Function `f` is not applicable to element {element}.")
            sys.exit(1)
        except ValueError:
            print(f"Error: Invalid value encountered for element {element}.")
            sys.exit(1)
        except Exception as e:  # Catch unexpected exceptions
            print(f"Unexpected error: {e}")
            sys.exit(1)
    return dictionary


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))
