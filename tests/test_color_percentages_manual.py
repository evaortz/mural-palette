from mural_analyzer.core.color_percentages import color_percentages
from mural_analyzer.core.quantizer import quantize_image
from mural_analyzer.core.image_loader import load_and_format
from PIL import Image

print("=" * 50)
print("Test 1: A good use of the function")
print("=" * 50)

#Example of a good use of the function
try:
    quantized_image = quantize_image(load_and_format("assets/samples/sketch1.jpeg", 800), 16)
    quantized_image[0].save("assets/samples/sketch1_quantized.png")
    percentages = color_percentages(quantized_image[0], quantized_image[1])
    assert isinstance(percentages, list), "The result is not a list"
    for color, percentage in percentages:
        assert isinstance(color, tuple), "The color is not a tuple"
        assert len(color) == 3, "The color tuple does not have three elements"
        for rgb_value in color:
            assert isinstance(rgb_value, int), "The RGB value is not an integer"
            assert 0 <= rgb_value <= 255, "The RGB value is not between 0 and 255"
        assert isinstance(percentage, float), "The percentage is not a float"
        assert 0 <= percentage <= 100, "The percentage is not between 0 and 100"
    print(f"Color percentages: {percentages}")
    print("Color percentages calculated successfully")
except AssertionError as e:
    print(f"Assertion error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 2: Test with a non-PIL.Image.Image file")
print("=" * 50)

#Test with a non-PIL.Image.Image file
try:
    color_percentages("assets/samples/sketch1_quantized.png", [(255, 0, 0), (0, 255, 0), (0, 0, 255)])
    print("No error was raised for a non-PIL.Image.Image file")
except TypeError as e:
    print(f"YES! - Expected error: {e}")


print("\n" + "=" * 50)
print("Test 3: Test with a non-list palette")
print("=" * 50)

#Test with a non-list palette
try:
    color_percentages(quantized_image[0], "not a list")
    print("No error was raised for a non-list palette")
except TypeError as e:
    print(f"YES! - Expected error: {e}")

print("\n" + "=" * 50)
print("Test 4: Test with a palette containing a non-tuple color")
print("=" * 50)

#Test with a palette containing a non-tuple color
try:
    color_percentages(quantized_image[0], [(255, 0, 0), "not a tuple", (0, 0, 255)])
    print("No error was raised for a palette containing a non-tuple color")
except TypeError as e:
    print(f"YES! - Expected error: {e}")


print("\n" + "=" * 50)
print("Test 5: Test with a palette containing a tuple with not three elements")
print("=" * 50)

#Test with a palette containing a tuple with not three elements
try:
    color_percentages(quantized_image[0], [(255, 0, 0), (0, 255), (0, 0, 255)])
    print("No error was raised for a palette containing a tuple with not three elements")
except ValueError as e:
    print(f"YES! - Expected error: {e}")


print("\n" + "=" * 50)
print("Test 6: Test with a palette containing a tuple with an RGB value not between 0 and 255")
print("=" * 50)

#Test with a palette containing a tuple with an RGB value not between 0 and 255
try:
    color_percentages(quantized_image[0], [(255, 0, 0), (0, 256, 0), (0, 0, 255)])
    print("No error was raised for a palette containing a tuple with an RGB value not between 0 and 255")
except ValueError as e:
    print(f"YES! - Expected error: {e}")


print("\n" + "=" * 50)
print("Test 7: Test with a palette containing a tuple with an RGB value not an integer")
print("=" * 50)

#Test with a palette containing a tuple with an RGB value not an integer
try:
    color_percentages(quantized_image[0], [(255, 0, 0), (0, "not an integer", 0), (0, 0, 255)])
    print("No error was raised for a palette containing a tuple with an RGB value not an integer")
except ValueError as e:
    print(f"YES! - Expected error: {e}")


print("\n" + "=" * 50)
print("Test 8: Test with a quantized image with more colors than the palette")
print("=" * 50)

#Test with a quantized image with more colors than the palette
try:
    color_percentages(quantized_image[0], [(255, 0, 0), (0, 255, 0)])
    print("No error was raised for a quantized image with more colors than the palette")
except ValueError as e:
    print(f"YES! - Expected error: {e}")    