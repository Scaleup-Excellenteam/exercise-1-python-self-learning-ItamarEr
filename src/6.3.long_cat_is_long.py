def long_cat_is_long(text: str) -> dict:
    """
    :param text: string of text.
    :return: dictionary of words and their lengths.
    """
    text = ["".join([char.lower() for char in word if char.isalpha()]) for word in text.split()]
    return {word: len(word) for word in text}


if __name__ == '__main__':
    text = """
        You see, wire telegraph is a kind of a very, very long cat.
        You pull his tail in New York and his head is meowing in Los Angeles.
        Do you understand this?
        And radio operates exactly the same way:
        you send signals here, they receive them there.
        The only difference is that there is no cat.
        """
    print(long_cat_is_long(text))
