from mural_analyzer.core.pipeline import analyze_image
from mural_analyzer.core.circle_packing import pack_circles


print("=" * 50)
print("Test with sample image: sketch1.jpeg")
print("=" * 50)

try:
    palette_info = analyze_image("assets/samples/sketch1.jpeg", 800, 13, 30)
    palette_circles_info = pack_circles(palette_info)

    # Structure asserts
    assert isinstance(palette_circles_info, list), "Result should be a list"
    assert len(palette_circles_info) == len(palette_info), "Palette circles info should have the same length as palette info"
    for i, circle_dict in enumerate(palette_circles_info):
        assert isinstance(circle_dict, dict), f"Circle {i} should be a dict"
        assert "rgb" in circle_dict, f"Circle {i} missing 'rgb'"
        assert "percentage" in circle_dict, f"Circle {i} missing 'percentage'"
        
        assert "cmyw" in circle_dict, f"Circle {i} missing 'cmyw'"
        assert "circle" in circle_dict, f"Circle {i} missing 'circle'"

        assert isinstance(circle_dict["circle"], dict), f"Circle {i} 'circle' should be a dict"
        for key in ["x", "y", "r"]:
            assert key in circle_dict["circle"], f"Circle {i} 'circle' missing key '{key}'"

    max_percentage = max(palette_circles_info, key=lambda item: item["percentage"])
    max_radius = max(palette_circles_info, key=lambda item: item["circle"]["r"])
    assert max_percentage["percentage"] == max_radius["percentage"], "The circle with the largest radius should correspond to the color with the highest percentage"
        
    print("YES! Circle packing test passed successfully.")

except AssertionError as e:
    print(f"Assertion error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
