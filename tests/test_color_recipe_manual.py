from mural_analyzer.core.image_loader import load_and_format
from mural_analyzer.core.quantizer import quantize_image
from mural_analyzer.core.color_merger import merge_colors
from mural_analyzer.core.color_percentages import color_percentages
from mural_analyzer.core.color_recipe import rgb_to_cmyw

print("=" * 50)
print("Test 1: A good use of the function")
print("=" * 50)

#Example of a good use of the function
try:
    quantized_image = quantize_image(load_and_format("assets/samples/sketch1.jpeg", 800), 10)
    quantized_image[0].save("assets/samples/sketch1_quantized.png")
    palette = quantized_image[1]
    assert isinstance(palette, list), "The palette is not a list"

    cmyw_palette = []

    for rgb_tuple in palette:
        assert isinstance(rgb_tuple, tuple), "The element is not a tuple"
        assert len(rgb_tuple) == 3, "The tuple does not have 3 elements"
        for rgb_value in rgb_tuple:
            assert 0 <= rgb_value <= 255, "The value is not in the range 0-255"
        cmyw_palette.append(rgb_to_cmyw(rgb_tuple))
    
    assert isinstance(cmyw_palette, list), "The returned palette is not a list"
    for cmyw_color in cmyw_palette:
        assert isinstance(cmyw_color, dict), "The color in the returned palette is not a dictionary"
        C, M, Y = cmyw_color["C"], cmyw_color["M"], cmyw_color["Y"]  
        assert abs((C + M + Y) - 100) < 0.5, "The sum of C + M + Y is not aprox 100"
        assert 0 <= cmyw_color["W"] <= 100, "The W value is not between 0 and 100"
    print(f"Colors recipes: {cmyw_palette}")
    print("Color recipes calculated successfully")
except AssertionError as e:
    print(f"Assertion error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")


print("=" * 50)
print("Test 2: Test with pure white")
print("=" * 50)

#Test with pure white
try:
    cmyw_color = rgb_to_cmyw((255, 255, 255))
    assert isinstance(cmyw_color, dict),"Result is not a dict"
    assert cmyw_color["C"] == cmyw_color["M"] == cmyw_color["Y"] == 0 and cmyw_color["W"] == 100, "The result is not the expected values"
    print(f"YES! - Pure white handled correctly: {cmyw_color}")
except AssertionError as e:
    print(f"NO - AssertionError error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")


print("=" * 50)
print("Test 3: Test with pure black")
print("=" * 50)

#Test with pure black
try:
    cmyw_color = rgb_to_cmyw((0, 0, 0))
    assert isinstance(cmyw_color, dict),"Result is not a dict"
    assert cmyw_color["C"] == cmyw_color["M"] == cmyw_color["Y"] == 33.3 and cmyw_color["W"] == 0, "The result is not the expected values"
    print(f"YES! - Pure black handled correctly: {cmyw_color}")
except AssertionError as e:
    print(f"NO - AssertionError error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")


print("\n" + "=" * 50)
print("Test 4: Test with a non-tuple rgb_tuple")
print("=" * 50)

#Test with a non-tuple rgb_tuple
try:
    rgb_to_cmyw(0)
    print("No error was raised for a non-tuple")
except TypeError as e:
    print(f"YES! - Expected TypeError: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")


print("\n" + "=" * 50)
print("Test 5: Test with a non-interger elements in rgb_tuple")
print("=" * 50)

#Test with a non-interger elements in rgb_tuple
try:
    rgb_to_cmyw(("a", "b", "c"))
    print("No error was raised for non-interger elements")
except TypeError as e:
    print(f"YES! - Expected TypeError: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")


print("\n" + "=" * 50)
print("Test 6: Test with a rgb_tuple that does not have exactly 3 elements")
print("=" * 50)

#Test with a rgb_tuple that does not have exactly 3 elements
try:
    rgb_to_cmyw((20, 20, 20, 20))
    print("No error was raised for a rgb_tuple with not exactly 3 elements")
except ValueError as e:
    print(f"YES! - Expected ValueError: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")


print("\n" + "=" * 50)
print("Test 7: Test with a rgb_tuple with a value not in the range 0-255")
print("=" * 50)

#Test with a rgb_tuple with a value not in the range 0-255
try:
    rgb_to_cmyw((256, 20, 20))
    print("No error was raised for a rgb_tuple with a value not in the range 0-255")
except ValueError as e:
    print(f"YES! - Expected ValueError: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")

