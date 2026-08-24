from mural_analyzer.core.image_loader import load_and_format
from mural_analyzer.core.quantizer import quantize_image
from PIL import Image


print("=" * 50)
print("Test 1: A good use of the function")
print("=" * 50)

#Example of a good use of the function
try:

    quantized_image = quantize_image(load_and_format("assets/samples/sketch1.jpeg", 800), 16)
    assert isinstance(quantized_image[0], Image.Image), "The quantized image is not a PIL Image object"
    assert isinstance(quantized_image[1], list), "The palette is not a list"
    assert quantized_image[0].mode == 'P', "The quantized image is not in 'P' mode"
    assert len(quantized_image[1]) <= 16, "The palette does not have the correct number of colors"
    quantized_image[0].save("assets/samples/sketch1_quantized.png")
    print("Image quantized successfully and saved as sketch1_quantized.png")
except AssertionError as e:
    print(f"Assertion error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")

print("\n" + "=" * 50)
print("Test 2: Test with a non-PIL.Image.Image file")
print("=" * 50)

#Test with a non-PIL.Image.Image file
try: 
    quantize_image("assets/samples/sketch1.jpeg", 16)
    print("It did not raise an error for a non-PIL.Image.Image file")
except TypeError as e:
    print(f"YES! - Expected error: {e}")

print("\n" + "=" * 50)
print("Test 3: Test with a non-integer n_colors")
print("=" * 50)

#Test with a non-integer n_colors
try: 
    quantize_image(load_and_format("assets/samples/sketch1.jpeg", 800), "hi")
    print("It did not raise an error for a non-integer n_colors")
except TypeError as e:
    print(f"YES! - Expected error: {e}")


print("\n" + "=" * 50)
print("Test 4: Test with a negative n_colors")
print("=" * 50)

#Test with a negative n_colors
try: 
    quantize_image(load_and_format("assets/samples/sketch1.jpeg", 800), -16)
    print("It did not raise an error for a negative n_colors")
except ValueError as e:
    print(f"YES! - Expected error: {e}")

print("\n" + "=" * 50)
print("Test 5: Test with a n_colors greater than 256")
print("=" * 50)

#Test with a n_colors greater than 256
try: 
    quantize_image(load_and_format("assets/samples/sketch1.jpeg", 800), 257)
    print("It did not raise an error for a n_colors greater than 256")
except ValueError as e:
    print(f"YES! - Expected error: {e}")


print("\n" + "=" * 50)
print("Test 6: Test with a n_colors equal to 0")
print("=" * 50)

#Test with a n_colors equal to 0
try: 
    quantize_image(load_and_format("assets/samples/sketch1.jpeg", 800), 0)
    print("It did not raise an error for a n_colors equal to 0")
except ValueError as e:
    print(f"YES! - Expected error: {e}")

print("\n" + "=" * 50)
print("Test 7: Test with a PIL.Image.Image with less colors than n_colors")
print("=" * 50)

#Test with a PIL.Image.Image with less colors than n_colors
try:
    three_colors_image = Image.new('RGB', (100, 100), color = (255, 0, 0))
    three_colors_image.paste((0, 255, 0), [0, 0, 25, 100])
    three_colors_image.paste((0, 0, 255), [25, 0, 50, 100])
    assert isinstance(three_colors_image, Image.Image), "The image is not a PIL Image object"
    quantized_image = quantize_image(three_colors_image, 16)
    assert isinstance(quantized_image[0], Image.Image), "The quantized image is not a PIL Image object"
    assert isinstance(quantized_image[1], list), "The palette is not a list"
    assert quantized_image[0].mode == 'P', "The quantized image is not in 'P' mode"
    assert len(quantized_image[1]) == 3, "The palette does not have the correct number of colors"
    quantized_image[0].save("assets/samples/three_colors_quantized.png")
    print("Image quantized successfully and saved as three_colors_quantized.png")
except AssertionError as e:
    print(f"Assertion error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
