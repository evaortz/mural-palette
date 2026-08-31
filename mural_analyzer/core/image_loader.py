import PIL
from PIL import Image

def open_image(fp):
    """opens an image and returns it as a PIL Image object

        Args:
            fp: acepts string, pathlib.Path object or file object
    """
    
    image = Image.open(fp)
    return image


def check_rgb(image):
    "checks if the image is in RGB format, if not it converts it to RGB"

    if not isinstance(image, Image.Image):
        raise TypeError("The image must be a PIL Image object")
    if image.mode != 'RGB':
        image = image.convert('RGB')
    return image

def resize_image(image, size):
    "resizes the image to the given pexels size as a maximus size, keeping the aspect ratio"

    if not isinstance(image, Image.Image):
        raise TypeError("The image must be a PIL Image object")
    if not isinstance(size, int):
        raise TypeError("The size must be an integer")
    if size <= 0:
        raise ValueError("The size must be a positive integer")
    if size > 10000:
        raise ValueError("The size must be less than 10000")
    image.thumbnail((size, size), resample=Image.LANCZOS)
    
    return image

def load_and_format(fp, size=800):
    """
    Load an check the format of an image, then it converts it to RGB if necesary and resizes it to the second parameter

        Args:
            fp: acepts string, pathlib.Path object or file object.
            size (int): Maximum width or height to resize the image to, maintaining aspect ratio. Default is 800.
    """

    image = open_image(fp)
    image = check_rgb(image)
    image = resize_image(image, size)
    return image