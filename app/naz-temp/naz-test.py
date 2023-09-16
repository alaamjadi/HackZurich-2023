import pytesseract
from PIL import Image

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
