"""
This is a simple crawler that you can use as a boilerplate for your own
implementation. The crawler labels `.txt` files that contain the word
"hello" as "true", `.txt` files without "hello" as "false" and every other
item as "review". Try to modify this simple implementation so that it finds
some sensitive data and then expand your crawler from there.

You can change the code however you want, just make sure that following
things are satisfied:

- Grab the files from the directory "../files" relative to this script
- If you use Python packages, add a "requirements.txt" to your submission
- If you need to download larger files, e.g. NLP models, don't add them to
  the `app` folder. Instead, download them when the Docker image is build by
  changing the Docker file.
- Save your labels as a pickled dictionary in the `../results` directory.
  Use the filename as the key and the label as the value for each file.
- Your code cannot the internet during evaluation. Design accordingly.
"""

import os
from pathlib import Path
import pickle
import pandas as pd
import numpy as np

from PIL import Image, ImageEnhance, ImageFilter
import pytesseract

from pathlib import Path
import re
from typing import Union
import PyPDF2

import extract_msg
import magic

import speech_recognition as sr
from pydub import AudioSegment

from docx import Document
from bs4 import BeautifulSoup
from markdown import markdown

from pathlib import Path
from typing import Union

from zipfile import ZipFile
import xml.etree.ElementTree as ET


class PdfHandler:
    """excepts a Path or str to a pdf file and flags is true (contains sensitive data)
    or false (does not contain sensitive data)"""

    def __call__(self, path: Union[str, Path]) -> bool:
        file_obj = open(path, "rb")
        pdf_reader = PyPDF2.PdfReader(file_obj)

        head = " ".join(pdf_reader.pages[0].extract_text().split(" ")[:3])
        print(head)
        if head == "Financial Analysis Report":
            is_sensitive = False

        elif "arXiv" in head:
            is_sensitive = False

        else:
            # process first page
            try:
                first = pdf_reader.pages[0].annotations[0].get_object()["/V"]
                last = pdf_reader.pages[0].annotations[1].get_object()["/V"]
                street = pdf_reader.pages[0].annotations[2].get_object()["/V"]
                city = pdf_reader.pages[0].annotations[3].get_object()["/V"]
                country = pdf_reader.pages[0].annotations[4].get_object()["/V"]
                zipcode = pdf_reader.pages[0].annotations[5].get_object()["/V"]

                # print(first, last, street, city, country, zipcode)
            except Exception as e:
                # raise e
                pass

            # process second page
            try:
                text = pdf_reader.pages[1].extract_text()
                hits = {}
                text_items = text.split("\n")

                for i, item in enumerate(text_items[:-1]):
                    if item in [
                        "Company Name:",
                        "Type of Company:",
                        "Ownership Structure:",
                        "Date of Birth:",
                        "Name:",
                    ]:
                        hits[item] = text_items[i + 1]
                    if item in ["Client Information:"]:
                        hits[item] = text_items[i + 1 : i + 3]

                # print(hits)

                # detect sensitive data
                has_full_name = self.is_full_name(first, last)
                if not has_full_name:
                    if hits.get("Name:"):
                        name = hits["Name:"].split(" ")
                        if len(name) >= 2:
                            first = name[0]
                            last = name[1]
                        has_full_name = self.is_full_name(first, last)

                has_address = self.is_address(street, city, country, zipcode)

                if hits.get("Company Name:"):
                    has_company_name = self.is_company_name(hits.get("Company Name:"))
                else:
                    has_company_name = False

                if hits.get("Date of Birth:"):
                    has_dob = self.is_data_of_birth(hits.get("Date of Birth:"))
                else:
                    has_dob = False

                # flag true or false
                has_primary = int(has_full_name) + int(has_company_name)

                if has_primary >= 2:
                    is_sensitive = True
                elif has_primary == 1 and (has_dob or has_address):
                    is_sensitive = True
                else:
                    is_sensitive = False

                # print(is_sensitive)
                # print(first, last)
                # print("__")
                # print(has_full_name)
                # print(text)
                # print(has_address)
                # print(has_dob)

                # print(" ")

            except Exception as e:
                print(path)
                print(e)
                raise e

        return is_sensitive

    @staticmethod
    def is_data_of_birth(dob: str):
        if dob:
            dob_list = dob.split(" ")
            if len(dob_list) == 2:
                _, date_str = dob.split(" ")
                pattern = r"^\d{4}-\d{2}-\d{2}$"
                return bool(re.match(pattern, date_str))

            else:
                return False
        else:
            return False

    @staticmethod
    def is_company_name(company_name: str):
        if company_name:
            return True
        else:
            return False

    @staticmethod
    def is_address(street: str, city: str, country: str, zipcode: str):
        if street and city and country and zipcode:
            return True
        else:
            return False

    @staticmethod
    def is_full_name(first: str, last: str):
        if first and last:
            return True
        else:
            return False



def save_dict_as_pickle(labels, filename):
    with open(filename, "w+b") as handle:
        pickle.dump(labels, handle, protocol=pickle.HIGHEST_PROTOCOL)
    handle.close()
    
    # import pandas as pd
    # with open(filename, "rb") as f:
    #     object = pickle.load(f)
    # df = pd.DataFrame([object])
    # df = df.transpose()
    # df.to_csv('../results/prettyResults.csv')


def im2text(im):
    im = Image.open(im)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save("temp.jpg")
    text = pytesseract.image_to_string(Image.open('temp.jpg'))
    return text


def classifier(file_path):
    # Check the data type








            mime_type = magic.Magic()
            file_extension = mime_type.from_buffer(attachment.data)
            
            if file_extension.startswith("text"):
                file_extension = ".txt"
            elif file_extension.startswith("PDF"):
                file_extension = ".pdf"
            elif file_extension.startswith("Microsoft Excel"):
                file_extension = ".xlsx"
            elif file_extension.startswith("PNG"):
                file_extension = ".png"
            else:
                # Use a generic extension if the type is unknown
                file_extension = ".bin"











    if file_path.suffix == ".txt":
        # Open the file to read out the content
        with open(file_path, encoding='utf-8') as f:
            
            file_content = f.read()
            f.close()
            # If the file contains the word "hello" label it as true
            if file_content.find("hello") != -1:
                return "True"
            else:
                return "False"
    else:
        # If it is not a `.txt` file the set the label to "review"
        return "review"

## extract zip files
# Define the source directory where zip files are located
source_directory = "/root/files"

# Define the destination directory where all zip files will be extracted
destination_directory = "/root/files/extracted_attachments"

# Ensure the destination directory exists, or create it if necessary
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

def extract_zip_files_recursively(directory):
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith(".zip"):
                zip_file_path = os.path.join(root, filename)
                
                try:
                    with ZipFile(zip_file_path, 'r') as zip_ref:
                        zip_ref.extractall(destination_directory)
                    print(f"Files from '{zip_file_path}' successfully extracted to '{destination_directory}'")
                except Exception as e:
                    print(f"An error occurred while extracting '{zip_file_path}': {str(e)}")

# Call the function to extract zip files recursively
extract_zip_files_recursively(source_directory)


## EXTRACT TXT FILES FROM MP3 FILES
def convert_mp3_to_text(source_directory, destination_directory):
    try:
        # Convert MP3 to WAV
        sound = AudioSegment.from_mp3(source_directory)
        sound.export(destination_directory, format="wav")

        # Create an AudioFile object using the WAV file
        file_audio = sr.AudioFile(destination_directory)

        # Initialize the recognizer
        r = sr.Recognizer()

        # Use the audio file as the audio source
        with file_audio as source:
            audio_text = r.record(source)

        try:
            # Recognize the audio
            recognized_text = r.recognize_google(audio_text)
            return recognized_text
        except sr.UnknownValueError:
            return "Speech Recognition could not understand audio"
    except Exception as e:
        return f"An error occurred: {str(e)}"

recognized_text = convert_mp3_to_text(input_mp3, output_wav)

# Create the output directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Create a unique text file name based on the input MP3 file name
output_txt_file = os.path.join(destination_directory, os.path.splitext(os.path.basename(input_mp3))[0] + ".txt")

# Write the recognized text to the text file
with open(output_txt_file, "w") as txt_file:
    txt_file.write(recognized_text)



# Function to extract .txt file and attachments from an .msg file
def extract_msg_file(source_directory, destination_directory):
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(destination_directory):
            os.makedirs(destination_directory)

        # Open the .msg file
        msg = extract_msg.Message(source_directory)

        # Extract the .txt file (if it exists)
        if msg.subject:
            txt_file_path = os.path.join(destination_directory, f"{msg.subject}.txt")
            with open(txt_file_path, "wb") as txt_file:
                txt_file.write(msg.body.encode('utf-8'))

        # Extract attachments (if any)
        for i, attachment in enumerate(msg.attachments):
            # Determine the file extension based on magic bytes
            mime_type = magic.Magic()
            file_extension = mime_type.from_buffer(attachment.data)
            
            if file_extension.startswith("text"):
                file_extension = ".txt"
            elif file_extension.startswith("PDF"):
                file_extension = ".pdf"
            elif file_extension.startswith("Microsoft Excel"):
                file_extension = ".xlsx"
            elif file_extension.startswith("PNG"):
                file_extension = ".png"
            else:
                # Use a generic extension if the type is unknown
                file_extension = ".bin"
            
            # Specify the filename based on attachment position
            attachment_name = f"attachment_{i + 1}{file_extension}"
            attachment_path = os.path.join(destination_directory, attachment_name)
            with open(attachment_path, "wb") as attachment_file:
                attachment_file.write(attachment.data)

        print(f"Files extracted to {destination_directory}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

extract_msg_file(source_directory, destination_directory)




# DOCX to text file conversion
# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith('.docx'):
        # Construct the full path to the DOCX file
        docx_filename = os.path.join(source_directory, filename)

        # Extract the base file name (without extension) from the DOCX file name
        base_filename = os.path.splitext(os.path.basename(docx_filename))[0]

        # Create the text file name by adding the ".txt" extension
        output_filename = os.path.join(destination_directory, base_filename + '.txt')

        # Initialize a Document object
        doc = Document(docx_filename)

        # Initialize an empty string to store the extracted text
        text = ''

        # Iterate through paragraphs in the document and extract text
        for paragraph in doc.paragraphs:
            text += paragraph.text + '\n'

        # Save the extracted text to the text file
        with open(output_filename, 'w', encoding='utf-8') as file:
            file.write(text)

        # Confirm that the text has been saved to the file
        print(f"Text from '{docx_filename}' has been saved to '{output_filename}'")



## HTML TO TXT CONVERSION
def extract_text_from_html(input_html_file, output_text_file):
    # Read the HTML content from the input file
    with open(input_html_file, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Get the text content from the HTML and replace newlines with spaces
    text_content = soup.get_text().replace('\n', ' ')

    # Save the text content to the output text file
    with open(output_text_file, "w", encoding="utf-8") as file:
        file.write(text_content)

    # Print a confirmation message
    print(f"Text has been extracted from '{input_html_file}' (newlines replaced with spaces) and saved to '{output_text_file}'")

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith('.html'):
        # Construct the full paths for input and output files
        input_html_file = os.path.join(source_directory, filename)
        output_text_file = os.path.join(destination_directory, os.path.splitext(filename)[0] + '.txt')

        # Extract text from the HTML file and save it to the text file
        extract_text_from_html(input_html_file, output_text_file)


## MD TO TXT FILE CONVERSION
def try_decode(bytes_content, encodings):
    for encoding in encodings:
        try:
            decoded_content = bytes_content.decode(encoding)
            return decoded_content
        except UnicodeDecodeError:
            continue
    return None

def markdown_to_text_file(input_filename, output_filename):
    # Read Markdown content from the input file as bytes
    with open(input_filename, 'rb') as input_file:
        markdown_bytes = input_file.read()

    # List of encodings to try (add more encodings as needed)
    encodings_to_try = ['utf-8', 'latin-1']  # You can extend this list with other encodings

    # Attempt to decode the bytes using different encodings
    markdown_content = try_decode(markdown_bytes, encodings_to_try)

    if markdown_content is None:
        print(f"Error: Unable to decode {input_filename} with the specified encodings.")
        return

    # Convert Markdown to HTML
    html = markdown(markdown_content)

    # Use BeautifulSoup to extract text from HTML
    soup = BeautifulSoup(html, "html.parser")
    text = ''.join(soup.findAll(string=True))

    # Write the text to the output file
    with open(output_filename, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith('.md'):
        # Construct the full paths for input and output files
        input_filename = os.path.join(source_directory, filename)
        output_filename = os.path.join(destination_directory, os.path.splitext(filename)[0] + '.txt')

        # Convert Markdown to text and save it to the text file
        markdown_to_text_file(input_filename, output_filename)


## XML TO TXT CONVERSION -> ONLY THING NOT WORKING PROPERLY
def convert_xml_to_txt(input_xml_filename, output_txt_filename):
    try:
        # Parse the XML file
        tree = ET.parse(input_xml_filename)

        # Convert the parsed XML to plain text without newlines
        notags = ET.tostring(tree.getroot(), encoding='utf-8', method='text')
        text_content = notags.decode('utf-8').replace('\n', '')  # Remove newlines

        # Remove excess whitespace (spaces, tabs, and multiple consecutive spaces)
        text_content = re.sub(r'\s+', ' ', text_content)

        # Write the text to the output file
        with open(output_txt_filename, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text_content.strip())  # Strip leading/trailing spaces

        print(f"XML file '{input_xml_filename}' successfully converted to '{output_txt_filename}'")

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Iterate through XML files in the source directory
for filename in os.listdir(source_directory):
    if filename.endswith('.xml'):
        # Construct the full paths for input and output files
        input_xml_filename = os.path.join(source_directory, filename)
        output_txt_filename = os.path.join(destination_directory, os.path.splitext(filename)[0] + '.txt')

        # Convert XML to text and save it to the text file
        convert_xml_to_txt(input_xml_filename, output_txt_filename)


## CONVERT IMG FILES TO TXT
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

# Create the destination directory if it doesn't exist
if not os.path.exists(destination_directory):
    os.makedirs(destination_directory)

# Iterate through files in the source directory
for filename in os.listdir(source_directory):
    file_extension = os.path.splitext(filename)[1].lower()

    # Check if the file extension is in the list of supported extensions
    if file_extension in image_extensions:
        # Construct the full paths for input and output files
        input_image_path = os.path.join(source_directory, filename)
        output_txt_filename = os.path.join(destination_directory, os.path.splitext(filename)[0] + '.txt')

        # Perform OCR on the image and save the extracted text to the text file
        extracted_text = ocr_image(input_image_path)
        
        # Write the extracted text to the output file
        with open(output_txt_filename, 'w', encoding='utf-8') as txt_file:
            txt_file.write(extracted_text)
        
        print(f"Image file '{input_image_path}' successfully converted to '{output_txt_filename}'")


# def evaluator(actual, prediction, file_dir_path):
#     official_score = 0    
#     print(actual)
#     print()
#     print(prediction)
#     for file_name in os.listdir(str(file_dir_path)+"/results"):
#         gt = actual.iloc[file_name]
#         pred = predict.iloc[file_name]

#         if actual=="TRUE" and pred=="TRUE":
#             official_score += 20
#         elif actual=="TRUE" and pred=="FALSE":
#             official_score -= 20
#         elif actual=="TRUE" and pred=="REVIEW":
#             official_score += 10
#         elif actual=="FALSE" and pred=="TRUE":
#             official_score -= 2
#         elif actual=="FALSE" and pred=="FALSE":
#             official_score += 2
#         elif actual=="FALSE" and pred=="REVIEw":
#             official_score -= 1
#     return official_score

#     yes, no = 0, 0
#     testRows = X.shape[0]

#     for i in range(testRows):
#         fv = X[i]                
#         actual = y[i]
#         prediction = predict(fv, W)

#         if actual == prediction:
#             yes += 1
#         else:
#             no += 1
#     score = (yes/(yes+no)) * 100 
#     return score, no


def main():
    # Get the path of the directory where this script is in
    script_dir_path_parent = Path(os.path.realpath(__file__)).parents[1]
    # Get the path containing the files that we want to label
    file_dir_path = script_dir_path_parent / "files"

    if os.path.exists(file_dir_path):
        # Initialize the label dictionary
        labels = {}

        # Loop over all items in the file directory
        for file_name in os.listdir(file_dir_path):
            file_path = file_dir_path / file_name
            labels[file_name] = classifier(file_path)

        # Save the label dictionary as a Pickle file
        save_dict_as_pickle(labels, script_dir_path_parent / 'results' / 'crawler_labels.pkl')
    else:
        output_dir = script_dir_path_parent / 'results'
        os.makedirs(output_dir, exist_ok=True)
        save_dict_as_pickle(labels, output_dir / 'crawler_labels.pkl')
        print("Please place the files in the corresponding folder")

    # gt = pd.read_csv(str(script_dir_path_parent) +"/results/labels.csv", header=0)
    # pred = pd.read_pickle(str(script_dir_path_parent) +"/results/crawler_labels.pkl")
    # pred = pd.DataFrame.from_dict(pred, orient='index')
    # print(pred)
    # print(evaluator(gt, pred,script_dir_path_parent))
    # print(accuracy(gt, pred))


if __name__ == "__main__":
    main()
