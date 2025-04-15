"""
This module extracts a hidden message from an image by its black pixels 
and their corresponding columns. Each black pixel in the image represents a character 
based on its row.
The function 'remember_remember' processes the image and extracts the message.
"""
from PIL import Image
BLACK_PIXEL = 1


def remember_remember(image_path):
    """
    Extracts a message from an image by the black pixels and their columns.
    :param image_path: path to an image.
    :return: the hidden message extracted from the image.
    """
    with Image.open(image_path) as img:
        width, height = img.size
        message = [
            chr(next((y for y in range(height) if img.getpixel((x, y)) == BLACK_PIXEL), 0))
            for x in range(width)
        ]

        return "".join(message)


if __name__ == "__main__":
    print(remember_remember("code.png"))
