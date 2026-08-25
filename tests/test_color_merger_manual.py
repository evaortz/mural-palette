from PIL import Image
from mural_analyzer.core.color_merger import merge_colors
from mural_analyzer.core.color_percentages import color_percentages
from mural_analyzer.core.quantizer import quantize_image
from mural_analyzer.core.image_loader import load_and_format

print("=" * 50)
print("Test 1: A good use of the function")
print("=" * 50)

#Example of a good use of the function
try:
    quantized_image = quantize_image(load_and_format("assets/samples/sketch1.jpeg", 800), 16)
    quantized_image[0].save("assets/samples/sketch1_quantized.png")
    percentages = color_percentages(quantized_image[0], quantized_image[1])
    merged_percentages = merge_colors(percentages, 10)
    assert isinstance(merged_percentages, list), "The result is not a list"
    for color, percentage in merged_percentages:
        assert isinstance(color, tuple), "The color is not a tuple"
        assert len(color) == 3, "The color tuple does not have three elements"
        for rgb_value in color:
            assert isinstance(rgb_value, int), "The RGB value is not an integer"
            assert 0 <= rgb_value <= 255, "The RGB value is not between 0 and 255"
        assert isinstance(percentage, float), "The percentage is not a float"
        assert 0 <= percentage <= 100, "The percentage is not between 0 and 100"
    print(f"Merged color percentages: {merged_percentages}")
    print("Color percentages merged successfully")
except AssertionError as e:
    print(f"Assertion error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

print("\n" + "=" * 50)
print("Test 2: Another good use of the function with simpler colors")
print("=" * 50)

#Another good use of the function with simpler colors
try:
    test_colors = [((255, 0, 0), 30.0), ((254, 0, 0), 20.0), ((100, 100, 100), 50.0)]
    merged_test_colors = merge_colors(test_colors, threshold=5)
    assert isinstance(merged_test_colors, list), "The result is not a list"
    for color, percentage in merged_test_colors:
        assert isinstance(color, tuple), "The color is not a tuple"
        assert len(color) == 3, "The color tuple does not have three elements"
        for rgb_value in color:
            assert isinstance(rgb_value, int), "The RGB value is not an integer"
            assert 0 <= rgb_value <= 255, "The RGB value is not between 0 and 255"
        assert isinstance(percentage, float), "The percentage is not a float"
        assert 0 <= percentage <= 100, "The percentage is not between 0 and 100"
    print(f"Merged test colors: {merged_test_colors}")
    print("Test colors merged successfully")
except AssertionError as e:
    print(f"Assertion error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 3: Different threshold values")
print("=" * 50)

# Test with different threshold values
try:
    test_colors = [((255, 0, 0), 30.0), ((0, 255, 0), 70.0)]
    merged_test_colors = merge_colors(test_colors, threshold=5)
    assert len(merged_test_colors) == 2, "Colors too different should NOT merge"
    assert merged_test_colors == test_colors, "Colors should remain unchanged"
    print(f"YES! - Colors too different did not merge as expected: {merged_test_colors}")
except AssertionError as e:
    print(f"Assertion error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 4: Test with an empty color_percentages_list")
print("=" * 50)

#Test with an empty color_percentages_list
try:
    merged_empty = merge_colors([], threshold=10)
    print("No error was raised for an empty color_percentages_list")
    assert merged_empty == [], "Empty list should remain empty"
    assert isinstance(merged_empty, list), "Result should be a list"
    print(f"YES! - Empty list handled correctly")
except AssertionError as e:
    print(f"Assertion error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 5: Test with a non-list color_percentages_list")
print("=" * 50)

#Test with a non-list color_percentages_list
try:
    merge_colors("not a list", threshold=10)
    print("No error was raised for a non-list color_percentages_list")
except Exception as e:
    print(f"YES! - Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 6: Test with a color_percentages_list containing a non-tuple item")
print("=" * 50)

#Test with a color_percentages_list containing a non-tuple item
try:
    merge_colors([((255, 0, 0), 30.0), "not a tuple", ((0, 255, 0), 70.0)], threshold=10)
    print("No error was raised for a color_percentages_list containing a non-tuple item")
except Exception as e:
    print(f"YES! - Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 7: Test with a color_percentages_list containing a tuple with not two elements")
print("=" * 50)

#Test with a color_percentages_list containing a tuple with not two elements
try:
    merge_colors([((255, 0, 0), 30.0), ((0, 255, 0),)], threshold=10)
    print("No error was raised for a color_percentages_list containing a tuple with not two elements")
except Exception as e:
    print(f"YES! - Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 8: Test with a color_percentages_list containing a tuple with a color that is not a tuple of three integers (R, G, B)")
print("=" * 50)

#Test with a color_percentages_list containing a tuple with a color that is not a tuple of three integers (R, G, B)
try:
    merge_colors([((255, 0, 0), 30.0), ("not a tuple", 70.0)], threshold=10)
    print("No error was raised for a color_percentages_list containing a tuple with a color that is not a tuple of three integers (R, G, B)")
except Exception as e:
    print(f"YES! - Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 9: Test with a color_percentages_list containing a tuple with a percentage that is not a non-negative number")
print("=" * 50)

#Test with a color_percentages_list containing a tuple with a percentage that is not a non-negative number
try:
    merge_colors([((255, 0, 0), -30.0), ((0, 255, 0), 70.0)], threshold=10)
    print("No error was raised for a color_percentages_list containing a tuple with a percentage that is not a non-negative number")
except Exception as e:
    print(f"YES! - Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 10: Test with a negative threshold")
print("=" * 50)

#Test with a negative threshold
try:
    merge_colors([((255, 0, 0), 30.0), ((0, 255, 0), 70.0)], threshold=-10)
    print("No error was raised for a negative threshold")
except Exception as e:
    print(f"YES! - Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 11: Test with a non-numeric threshold")
print("=" * 50)

#Test with a non-numeric threshold
try:
    merge_colors([((255, 0, 0), 30.0), ((0, 255, 0), 70.0)], threshold="not a number")
    print("No error was raised for a non-numeric threshold")
except Exception as e:
    print(f"YES! - Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 12: Test with a color_percentages_list containing a tuple with a color that has an RGB value not between 0 and 255")
print("=" * 50)

#Test with a color_percentages_list containing a tuple with a color that has an RGB value not between 0 and 255
try:
    merge_colors([((255, 0, 0), 30.0), ((0, 256, 0), 70.0)], threshold=10)
    print("No error was raised for a color_percentages_list containing a tuple with a color that has an RGB value not between 0 and 255")
except Exception as e:
    print(f"YES! - Unexpected error: {e}")