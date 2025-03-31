"""
This module provides a function to analyze text and return a dictionary 
where words are mapped to their lengths.
The function `long_cat_is_long` processes a given text by converting words 
to lowercase, removing non-alphabetic characters, and computing their lengths.
"""


def long_cat_is_long(text: str) -> dict:
    """
    Computes the length of each word in the given text.

    :param text: A string containing words.
    :return: A dictionary where keys are words (in lowercase, without punctuation) 
             and values are their lengths.
    """
    words = ["".join([char.lower() for char in word if char.isalpha()]) for word in text.split()]
    return {word: len(word) for word in words if word}


if __name__ == '__main__':
    sample_text = "The quick brown fox, jumps over the lazy dog."
    print(long_cat_is_long(sample_text))
