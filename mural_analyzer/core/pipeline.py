from mural_analyzer.core.image_loader import load_and_format
from mural_analyzer.core.quantizer import quantize_image
from mural_analyzer.core.color_merger import merge_colors
from mural_analyzer.core.color_percentages import color_percentages
from mural_analyzer.core.color_recipe import rgb_to_cmyw

def analyze_image(fp, size=800, n_colors=16, merge_threshold=20):
    """
    Quantizes an image to n_colors, merges similar colors, and extracts the palette in CMYW with percentages.

        Args:
            fp: acepts string, pathlib.Path object or file object.
            size (int): Maximum width or height to resize the image to, maintaining aspect ratio. Default is 800.
            n_colors (int): The number of colors to quantize the image to. Default is 16.
            merge_threshold (int): Maximum distance to consider two colors "similar" (0-255). Default is 20.
        
        Returns:
            list[dict]: List of dictionaries, each containing:
            - 'rgb' (tuple): RGB color (R, G, B) in range 0-255
            - 'percentage' (float): Percentage of image covered by this color
            - 'cmyw' (dict): Paint recipe with keys C, M, Y, W (all floats 0-100)
        
        Raises:
            FileNotFoundError: If the image file doesn't exist.
            ValueError: If parameters are invalid or image processing fails.
            TypeError: If parameter types are incorrect.
    """

    #1. Cargar imagen desde ruta → variable: img
    img = load_and_format(fp, size)

    #2. Cuantizar a n_colors → variable: quantized_img, palette = quantize_image(...)
    quantized_img, palette = quantize_image(img, n_colors)

    #3. Extraer los porcentajes de cada color pasandole el PIL.Image.Image de la imagen quantizada y la paleta: color_percentages_list
    color_percentages_list = color_percentages(quantized_img, palette)

    #4. Mergear los colores parecidos según merge_threshold: merged_colors
    merged_colors = merge_colors(color_percentages_list, merge_threshold)

    #5. Hacer la conversion de los merged_colors a cmyw: palette_info
    palette_info = []
    for color, percentage in merged_colors:
        palette_info.append({"rgb": color, "percentage": percentage, "cmyw": rgb_to_cmyw(color)})


    return palette_info
    
   