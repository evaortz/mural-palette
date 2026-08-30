from mural_analyzer.core.pipeline import analyze_image

print("=" * 50)
print("Test 1: A good use of the function")
print("=" * 50)

try:
    palette_info = analyze_image("assets/samples/sketch1.jpeg", 800, 13, 30)


    # Structure asserts
    assert isinstance(palette_info, list), "Result should be a list"
    assert len(palette_info) > 0, "Palette should not be empty"
    
    # Each color asserts
    for i, color_dict in enumerate(palette_info):
        assert isinstance(color_dict, dict), f"Color {i} should be a dict"
        assert "rgb" in color_dict, f"Color {i} missing 'rgb'"
        assert "percentage" in color_dict, f"Color {i} missing 'percentage'"
        assert "cmyw" in color_dict, f"Color {i} missing 'cmyw'"
        
        assert isinstance(color_dict["rgb"], tuple), f"Color {i} rgb should be tuple"
        assert len(color_dict["rgb"]) == 3, f"Color {i} rgb should have 3 elements"
        
        assert isinstance(color_dict["percentage"], (int, float)), f"Color {i} percentage should be number"
        assert 0 <= color_dict["percentage"] <= 100, f"Color {i} percentage out of range"
        
        assert isinstance(color_dict["cmyw"], dict), f"Color {i} cmyw should be dict"
        assert set(color_dict["cmyw"].keys()) == {"C", "M", "Y", "W"}, f"Color {i} cmyw keys incorrect"

    print(f"Palette returned: {len(palette_info)} colors")
    print(f"Colors recipes: {palette_info}")
except Exception as e:
    print(f"Unexpected error: {e}")
