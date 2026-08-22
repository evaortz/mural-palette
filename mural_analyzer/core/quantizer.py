from PIL import Image

def quantize_image(image, n_colors=16):
    """
    Quantizes an image to a number of colors and returns the image and the palette.
    
    Args: 
        image (PIL.Image.Image): The image to quantize.
        n_colors (int): The number of colors to quantize the image to. Default is 16.

    Returns:
        quantized_image (PIL.Image.Image): The quantized image.
        palette (list of tuples): The palette of colors with the format (R, G, B). It can contain less than n_colors if the image has less colors.

    Raises:
        TypeError: If the image is not a PIL Image object or if n_colors is not an integer.
        ValueError: If n_colors is not a positive integer or if it is greater than 256.

    """
    if not isinstance(image, Image.Image):
        raise TypeError("The image must be a PIL Image object")
    if not isinstance(n_colors, int):
        raise TypeError("The number of colors must be an integer")  
    if n_colors <= 0:
        raise ValueError("The number of colors must be a positive integer")
    if n_colors > 256:
        raise ValueError("The number of colors must be less than or equal to 256")

    quantized_image = image.quantize(colors=n_colors, method=Image.MEDIANCUT, dither=Image.NONE)
    raw_palette = quantized_image.getpalette()
    color_counts = quantized_image.getcolors()

    palette = []

    for i in range(0, n_colors * 3, 3):
        palette.append((raw_palette[i], raw_palette[i + 1], raw_palette[i + 2]))

    used_colors = []
    for _, index in color_counts:
        used_colors.append(index)

    used_palette = []
    for index in used_colors:
        used_palette.append(palette[index])


    return quantized_image, used_palette