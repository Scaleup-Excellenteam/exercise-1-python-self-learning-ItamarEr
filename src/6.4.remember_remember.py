"""
This module extracts a hidden message from an image by its black pixels 
and their corresponding columns. Each black pixel in the image represents a character 
based on its row.
The function 'remember_remember' processes the image and extracts the message.
"""
from PIL import Image


def remember_remember(image_path):
    """
    Extracts a message from an image by the black pixels and their columns.
    :param image_path: path to an image.
    :return: the hidden message extracted from the image.
    """
    try:
        with Image.open(image_path) as img:
            width, height = img.size
            message = []
            for x in range(width):
                for y in range(height):
                    pixel_value = img.getpixel((x, y))
                    if pixel_value == 1:      # black pixel
                        message.append(chr(y))
                        break
            return "".join(message)

    except FileNotFoundError:
        print(f"File not found: {image_path}")
        return ""

if __name__ == "__main__":
    print(remember_remember("code.png"))
