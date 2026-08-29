def rgb_to_cmyw(rgb_tuple):
    """
    Converts an RGB color to its CMYW conversion.
        Arg:
            rgb_tuple: A tuple of three integers (R, G, B).
        Returns:
            A dictionary with the keys 'C', 'M', 'Y', and 'W' representing the corresponding CMYW values.
        Raises:
            TypeError: If the input is not a tuple or if any element is not an integer.
            ValueError: If the tuple does not contain exactly three elements or if any element is not in the range 0 -255.
    """
    if not isinstance(rgb_tuple, tuple):
        raise TypeError("The input must be a tuple")

    if len(rgb_tuple) != 3:
        raise ValueError("The input tuple must contain three elements")

    for element in rgb_tuple:
        if not isinstance(element, int):
            raise TypeError("Each element in the tuple must be an integer")
        if not (0 <= element <= 255):
            raise ValueError("Each integer in the tuple must be between 0 and 255")
    
    # Convert RGB to values between 0 and 1
    r = rgb_tuple[0] / 255.0 
    g = rgb_tuple[1] / 255.0
    b = rgb_tuple[2] / 255.0
    #Comon value of the 3 will be white
    w = min(r, g, b)

    #Full white exception
    if w >= 0.999:
        return {"C":0, "M":0, "Y":0, "W":100}

    #CMY conversion without introducting white, complementary equivalents
    c0 = 1 - r
    m0 = 1 - g
    y0 = 1 - b

    #Extract the comon value of the 3 tones(white) and left the real amount of pigment, as the cmyk conversion works but upside down
    c = c0 / (1 - w)
    m = m0 / (1 - w)
    y = y0 / (1 - w)

    #Get the percentage of each pigment
    total = c + m + y
    c_pct = (c / total) * 100
    m_pct = (m / total) * 100
    y_pct = (y / total) * 100
    w_pct = w * 100

    return {"C": round(c_pct, 1), "M": round(m_pct, 1), "Y": round(y_pct, 1), "W": round(w_pct, 1)}