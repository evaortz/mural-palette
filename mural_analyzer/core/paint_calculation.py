def calculate_palette_quantities(palette_info, total_area, coverage_rate=10):
    """Calculates surface (m²) and liters of mixture needed for each color in the palette.
    
    Args:
        palette_info (list): A list of dictionaries containing color information.
        total_area (float): The total area to be painted in square meters.
        coverage_rate (float): The coverage rate in m² per liter. Default is 10 m²/L.
        
    Returns:
        list: A list of dictionaries containing the calculated surface and liters for each color.
    """
    if total_area <= 0:
        raise ValueError("Total area must be a positive number.")
    if coverage_rate <= 0:
        raise ValueError("Coverage rate must be a positive number.")

    palette_quantities = []
    for color_info in palette_info:
        if 'percentage' not in color_info:
            raise ValueError("Each color_info dictionary must contain a 'percentage' key.")
        color_percentage = color_info['percentage']
        
        # Calculate the surface area for this color
        surface_area = (color_percentage / 100) * total_area
        
        # Calculate the liters needed for this color
        liters_needed = surface_area / coverage_rate
        
        color_info['surface'] = surface_area
        color_info['liters'] = liters_needed
        palette_quantities.append(color_info)
    return palette_quantities

def calculate_primary_quantities(palette_info):
    """Sums the liters of each primary color (C, M, Y, W) needed in the entire palette.
    
    Args:
        palette_info (list): A list of dictionaries containing color information including liters needed for each color.
        
    Returns:
        dict: A dictionary containing the total liters needed for each primary color.
    """
    primary_totals = {'C': 0, 'M': 0, 'Y': 0, 'W': 0}
    
    for color_info in palette_info:
        if 'cmyw' not in color_info or 'liters' not in color_info:
            raise ValueError("Each color_info dictionary must contain 'cmyw' and 'liters' keys.")
        cmyw = color_info['cmyw']
        liters = color_info['liters']
        
        primary_totals['C'] += (cmyw['C'] / 100) * liters
        primary_totals['M'] += (cmyw['M'] / 100) * liters
        primary_totals['Y'] += (cmyw['Y'] / 100) * liters
        primary_totals['W'] += (cmyw['W'] / 100) * liters
    
    return primary_totals