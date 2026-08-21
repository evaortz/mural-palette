from mural_analyzer.core.image_loader import load_and_format
from PIL import Image
from PIL import UnidentifiedImageError


#Example of a good use of the function
try: 
    load_and_format("assets/samples/sketch1.jpeg", 800)
    print("Image loaded and formatted successfully")
except Exception as e:
    print(f"Unexpected error: {e}")

#Test with a non-existent file
try: 
    load_and_format("assets/non_existent_file.jpeg", 800)
    print("It did not raise an error for a non-existent file")
except FileNotFoundError as e:
    print(f"YES! - Expected error: {e}")

#Test with a non-image file
try: 
    load_and_format("tests/test.txt", 800)
    print("It did not raise an error for a non-image file") 
except UnidentifiedImageError as e:
    print(f"YES! - Expected error: {e}")


#Test with a negative size
try: 
    load_and_format("assets/samples/sketch1.jpeg", -800)
    print("It did not raise an error for a negative size")
except ValueError as e:
    print(f"YES! - Expected error: {e}")

#Test with a size greater than 10000
try: 
    load_and_format("assets/samples/sketch1.jpeg", 10001)
    print("It did not raise an error for a size greater than 10000")
except ValueError as e:
    print(f"YES! - Expected error: {e}")