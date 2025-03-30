def parsle_tongue():
    """
    This function reads a file called "logo.jpg" and extracts the hidden message from it.
    The message is sequence of 5 or more lowercase english letters in a row separated by !.
    """
    filename = "logo.jpg"
    read_size = 1024
    message_min_size = 5

    try:
        with open(filename, 'rb') as file:  # Open the file in binary mode
            while True:
                data = file.read(read_size)       # Read the file in chunks of 1024 bytes
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
                        if char == "!" and len(message) >= message_min_size:
                            # If the character is !, yield the message if it is at least 5 characters long.
                            yield message
                            print(index)
                        message = ""

    except FileNotFoundError:
        print("File not found")


if __name__ == "__main__":
    gen = parsle_tongue()
    for word in gen:
        print(word)
