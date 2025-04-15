READ_SIZE = 1024
MESSAGE_MIN_SIZE = 5


def parsle_tongue():
    """
    This function reads a file called "logo.jpg" and extracts the hidden message from it.
    The message is sequence of 5 or more lowercase english letters in a row separated by !.
    """
    filename = "logo.jpg"

    with open(filename, 'rb') as file:  # Open the file in binary mode
        while True:
            data = file.read(READ_SIZE)       # Read the file in chunks of 1024 bytes
            if not data:
                break
            message = ""
            index = 0
            for char in data:
                char = chr(char)
                index += 1
                if char.isalpha() and char.islower() and char.isascii():
                    message += char       # Append the character if it is a lowercase english letter.

                else:
                    if char == "!" and len(message) >= MESSAGE_MIN_SIZE:
                        # If the character is !, yield the message if it is at least 5 characters long.
                        yield message
                    message = ""


def main():
    gen = parsle_tongue()
    for word in gen:
        print(word)


if __name__ == "__main__":
    main()
