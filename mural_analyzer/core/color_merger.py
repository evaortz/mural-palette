import math

def merge_colors(color_percentages_list, threshold=20):
    """
    Merges similar colors in the color percentages list based on a given threshold.
    
    Args:
        color_percentages_list: list of tuples with the format (color, percentage)
        threshold: maximum distance to consider two colors "similar" (0-255)
    
    Returns:
        list of merged tuples (fewer colors, combined percentages)
    """

    if not isinstance(color_percentages_list, list):
        raise TypeError("The color percentages list must be a list")
    for color_percentage in color_percentages_list:
        if not isinstance(color_percentage, tuple) or len(color_percentage) != 2:
            raise TypeError("Each item in the color percentages list must be a tuple of (color, percentage)")
        color, percentage = color_percentage
        if not isinstance(color, tuple) or len(color) != 3:
            raise TypeError("Each color must be a tuple of three integers (R, G, B)")
        for rgb_value in color:
            if not isinstance(rgb_value, int) or not (0 <= rgb_value <= 255):
                raise ValueError("Each RGB value must be an integer between 0 and 255")
        if not isinstance(percentage, (int, float)) or percentage < 0:
            raise ValueError("Percentage must be a non-negative number")

    if not isinstance(threshold, (int, float)) or threshold < 0:
        raise ValueError("Threshold must be a non-negative number")

    
    merged_colors = list(color_percentages_list)
    changes_made = False
    while True:
        auxiliary_list = []
        processed_indices = []
        changes_made = False
        for i in range(len(merged_colors)):
            if i in processed_indices:
                continue
            color1, percentage1 = merged_colors[i]
            fused = False
            
            for j in range(i + 1, len(merged_colors)):
                if j in processed_indices:
                    continue
                color2, percentage2 = merged_colors[j]
                distance = math.sqrt((color1[0]-color2[0])**2+(color1[1]-color2[1])**2+(color1[2]-color2[2])**2)
                if distance <= threshold:
                    if percentage1 >= percentage2:
                        new_color = color1
                    else:
                        new_color = color2
                    new_percentage = percentage1 + percentage2
                    auxiliary_list.append((new_color, new_percentage))
                    processed_indices.append(j)
                    changes_made = True
                    fused = True
                    break
            if not fused:
                auxiliary_list.append((color1, percentage1))
                
        merged_colors = auxiliary_list
        if not changes_made:
            break
    return merged_colors