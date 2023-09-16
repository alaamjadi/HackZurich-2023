import pytesseract
from PIL import Image

# Open an image
image = Image.open('temp.jpg')

# Perform OCR
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)
