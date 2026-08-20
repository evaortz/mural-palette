import PIL
from PIL import Image

def open_image(route):
    "opens an image and returns it as a PIL Image object"
    
    try: image = Image.open(route)
    except FileNotFoundError: 
        raise
    except PIL.UnidentifiedImageError:
        raise
    except PermissionError:
        raise

    return image


def check_rgb(image):
    "checks if the image is in RGB format, if not it converts it to RGB"

    if image.mode != 'RGB':
        image = image.convert('RGB')

    return image

def resize_image(image, size):
    "resizes the image to the given pexels size as a maximus size, keeping the aspect ratio"
    image.thumbnail((size, size), resample=Image.LANCZOS)
    

    return image

def load_and_format(route, size):
    "Load an check the format of an image, then it converts it to RGB if necesary and resizes it to the second parameter"