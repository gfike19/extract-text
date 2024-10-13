from PIL import Image
import pytesseract
import os

# List files in the data directory to ensure correct paths
files = os.listdir("/mnt/data/")
print(files)  # This step helps to identify the correct file name

# Load the image
image_path = "/mnt/data/image.png"
image = Image.open(image_path)

# Extract the text using pytesseract
text = pytesseract.image_to_string(image)

# Output the extracted text
print(text)
