import pytesseract
from PIL import Image
import magic

image_file = 'img.png'  # Change this to the path of your image file

# Function to perform OCR on an image
def ocr_image(image_path):
    try:
        # Open an image
        image = Image.open(image_path)

        # Perform OCR
        text = pytesseract.image_to_string(image)

        return text
    except Exception as e:
        return str(e)

# List of image file extensions to process
image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']


# Check if the file extension is in the list of supported extensions
file_extension = image_file.lower()
if any(file_extension.endswith(ext) for ext in image_extensions):
    extracted_text = ocr_image(image_file)
    print(extracted_text)
else:
    print("Unsupported image file format")




def get_file_type(file_path):
    # Create a magic object
    magic_obj = magic.Magic()

    # Use the magic object to identify the file type
    file_type = magic_obj.from_file(file_path)

    return file_type

# Example usage:
file_path = "path/to/your/file.ext"
file_type = get_file_type(file_path)
print(f"The file {file_path} is of type: {file_type}")