import circlify as circ

def pack_circles(palette_info):
    """
    Packs circles based on the sorted palette information.

    Args:
        palette_info (list): A list of dictionaries containing palette information, each with 'rgb','percentage' and 'cmyw' keys.

    Returns:
        palette_circles_info: A list of dictionaries containing ''rgb', 'percentage', 'cmyw' and 'circle' (with a dict with x, y, r) keys for each packed circle.
    """
    #1 Sort palette_info by percentage in descending order
    sorted_palette_info = sorted(palette_info, key=lambda item: item["percentage"], reverse=True)

    #2 Execute circle packing using circlify
    palette_circles = circ.circlify(sorted_palette_info, datum_field='percentage')

    #3 Parse the packed circles into a list of dictionaries with rgb, percentage, cmyk and circle (with a dict with x, y, r)
    palette_circles_info = []
    for circle in palette_circles:
        palette_circles_info.append({
            "rgb": circle.ex["rgb"],
            "percentage": circle.ex["percentage"],
            "cmyw": circle.ex["cmyw"],
            "circle": {
                "x": circle.x,
                "y": circle.y,
                "r": circle.r
            }
        })
    return palette_circles_info