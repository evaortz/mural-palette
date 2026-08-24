from PIL import Image

def color_percentages(quantized_image, palette):
    """
    Calculates the percentage of each color in the quantized image.

    Args:
        quantized_image (PIL.Image.Image): The quantized image.
        palette (list of tuples): The palette of colors with the format (R, G, B).

    Returns:
        color_percentages (list of tuples): A list of tuples where each tuple contains a color and its percentage in the image with the format (color, percentage).
    
    Raises:
        TypeError: If quantized_image is not a PIL Image object or if palette is not a list or if any color in the palette is not a tuple.
        ValueError: If there are not three integers (R, G, B), if any RGB value is not between 0 and 255 or if the number of colors in the quantized image exceeds the number of colors in the palette.
    """
    if not isinstance(quantized_image, Image.Image):
        raise TypeError("The quantized image must be a PIL Image object")
    if not isinstance(palette, list):
        raise TypeError("The palette must be a list")
    for color in palette:
        if not isinstance(color, tuple):
            raise TypeError("Each color in the palette must be a tuple of three integers (R, G, B)")
        if len(color) != 3:
            raise ValueError("Each color in the palette must be a tuple of three integers (R, G, B)")
        for rgb_value in color:
            if not isinstance(rgb_value, int) or not (0 <= rgb_value <= 255):
                raise ValueError("Each RGB value must be an integer between 0 and 255")


    image_width, image_height = quantized_image.size
    total_pixels = image_width * image_height
    percentages_list = []
    color_counts = quantized_image.getcolors()


    for count, index in color_counts:
        if index >= len(palette):
            raise ValueError("The number of colors in the quantized image exceeds the number of colors in the palette")
        percentages_list.append((palette[index], (count / total_pixels) * 100))

    return percentages_list
