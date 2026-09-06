from mural_analyzer.core.pipeline import analyze_image
from mural_analyzer.core.paint_calculation import calculate_palette_quantities, calculate_primary_quantities

print("=" * 50)
print("Test 1: A good use of the function")
print("=" * 50)

try:
    palette_info = analyze_image("assets/samples/sketch1.jpeg")
    total_area = 100 
    coverage_rate = 10
    palette_quantities = calculate_palette_quantities(palette_info, total_area, coverage_rate)
    assert isinstance(palette_quantities, list), "Result should be a list"
    assert len(palette_quantities) == len(palette_info), "Palette quantities should match the number of colors in the palette"
    primary_totals = calculate_primary_quantities(palette_quantities)
    assert isinstance(primary_totals, dict), "Primary totals should be a dictionary"
    assert all(isinstance(liters, (int, float)) for liters in primary_totals.values()), "Primary totals should be numeric"
    print(f"YES! Palette quantities and primary totals calculated successfully.")
    print("Palette Quantities:")
    for color in palette_quantities:
        print(f"  {color['rgb']}: {color['surface']:.2f} m², {color['liters']:.2f} L")
    print("Primary Totals:")
    for color, liters in primary_totals.items():
        print(f"  {color}: {liters:.2f} L")
except AssertionError as ae:
    print(f"Assertion error: {ae}")
except Exception as e:
    print(f"Unexpected error: {e}")


print("=" * 50)
print("Test 2: A good use of the function with mesureable parameters")
print("=" * 50)

try:
    palette_info = [{ "rgb": (255, 0, 0), "cmyw": {"C": 0, "M": 100, "Y": 100, "W": 0}, "percentage": 50 },
                    { "rgb": (0, 255, 0), "cmyw": {"C": 100, "M": 0, "Y": 100, "W": 0}, "percentage": 30 },
                    { "rgb": (0, 0, 255), "cmyw": {"C": 100, "M": 100, "Y": 0, "W": 0}, "percentage": 20 }]
    total_area = 10
    coverage_rate = 10
    palette_quantities = calculate_palette_quantities(palette_info, total_area, coverage_rate)
    assert palette_quantities[0]['surface'] == 5.0, "Surface area for first color should be 5.0 m²"
    assert palette_quantities[0]['liters'] == 0.5, "Liters needed for first color should be 0.5 L"
    assert palette_quantities[1]['surface'] == 3.0, "Surface area for second color should be 3.0 m²"
    assert palette_quantities[1]['liters'] == 0.3, "Liters needed for second color should be 0.3 L"
    assert palette_quantities[2]['surface'] == 2.0, "Surface area for third color should be 2.0 m²"
    assert palette_quantities[2]['liters'] == 0.2, "Liters needed for third color should be 0.2 L"

    primary_totals = calculate_primary_quantities(palette_quantities)
    print(f"YES! Palette quantities and primary totals calculated successfully.")
    print("Palette Quantities:")
    for color in palette_quantities:
        print(f"  {color['rgb']}: {color['surface']:.2f} m², {color['liters']:.2f} L")
    print("Primary Totals:")
    for color, liters in primary_totals.items():
        print(f"  {color}: {liters:.2f} L")
except AssertionError as ae:
    print(f"Assertion error: {ae}")
except Exception as e:
    print(f"Unexpected error: {e}")

print("=" * 50)
print("Test 3: Edge case with zero total area")
print("=" * 50)

try:
    palette_info = analyze_image("assets/samples/sketch1.jpeg")
    total_area = 0  
    coverage_rate = 10
    palette_quantities = calculate_palette_quantities(palette_info, total_area, coverage_rate)
except ValueError as ve:
    print(f"YES!-Expected error for zero total area: {ve}")
except Exception as e:
    print(f"Unexpected error: {e}")


print("=" * 50)
print("Test 4: Edge case with negative coverage rate") 
print("=" * 50)

try:
    palette_info = analyze_image("assets/samples/sketch1.jpeg")
    total_area = 100  
    coverage_rate = -5  
    palette_quantities = calculate_palette_quantities(palette_info, total_area, coverage_rate)
except ValueError as ve:
    print(f"YES!-Expected error for negative coverage rate: {ve}")
except Exception as e:
    print(f"Unexpected error: {e}")


