## extract zip files
import os
from zipfile import ZipFile

# Define the source directory where zip files are located
source_directory = "/root/Hackzurich/zip_files"

# Define the destination directory where all zip files will be extracted
destination_directory = "/root/Hackzurich/zip_attachments"

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


## extract text data from mp3 files
import speech_recognition as sr
from pydub import AudioSegment
import os

def convert_mp3_to_text(input_mp3_path, output_wav_path):
    try:
        # Convert MP3 to WAV
        sound = AudioSegment.from_mp3(input_mp3_path)
        sound.export(output_wav_path, format="wav")

        # Create an AudioFile object using the WAV file
        file_audio = sr.AudioFile(output_wav_path)

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

# Usage example:
input_mp3 = "/root/Hackzurich/ocpd_03_my_family.mpga"
output_wav = "/root/Hackzurich/ocpd_03_my_family.wav"
output_txt_dir = "mp3_txt_files"  # Directory to store text files

recognized_text = convert_mp3_to_text(input_mp3, output_wav)

# Create the output directory if it doesn't exist
if not os.path.exists(output_txt_dir):
    os.makedirs(output_txt_dir)

# Create a unique text file name based on the input MP3 file name
output_txt_file = os.path.join(output_txt_dir, os.path.splitext(os.path.basename(input_mp3))[0] + ".txt")

# Write the recognized text to the text file
with open(output_txt_file, "w") as txt_file:
    txt_file.write(recognized_text)



## extract text files and attachments from .msg files
import os
import extract_msg
import magic  # Install this library with 'pip install python-magic'

# Function to extract .txt file and attachments from an .msg file
def extract_msg_file(msg_file_path, output_dir):
    try:
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Open the .msg file
        msg = extract_msg.Message(msg_file_path)

        # Extract the .txt file (if it exists)
        if msg.subject:
            txt_file_path = os.path.join(output_dir, f"{msg.subject}.txt")
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
            attachment_path = os.path.join(output_dir, attachment_name)
            with open(attachment_path, "wb") as attachment_file:
                attachment_file.write(attachment.data)

        print(f"Files extracted to {output_dir}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")



# Usage example
msg_file_path = "incidunt-officia.msg"  # Replace with the path to your .msg file
output_dir = "msg_extracted_files"  # Directory to store extracted files

extract_msg_file(msg_file_path, output_dir)

# DOCX to text file conversion

from docx import Document

# Specify the absolute path to your Word document
docx_filename = '/root/Hackzurich/baby-thing-follow.docx'

# Initialize a Document object
doc = Document(docx_filename)

# Initialize an empty string to store the extracted text
text = ''

# Iterate through paragraphs in the document and extract text
for paragraph in doc.paragraphs:
    text += paragraph.text + '\n'

# Specify the path for the output text file
output_filename = '/root/Hackzurich/output.txt'

# Save the extracted text to a text file
with open(output_filename, 'w', encoding='utf-8') as file:
    file.write(text)

# Confirm that the text has been saved to the file
print(f"Text has been saved to '{output_filename}'")



## HTML TO TXT CONVERSION

from bs4 import BeautifulSoup

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

# Example usage of the function
input_html_file = "add-make-manager.html"
output_text_file = "output.txt"
extract_text_from_html(input_html_file, output_text_file)




## MD TO TXT FILE CONVERSION

from bs4 import BeautifulSoup
from markdown import markdown

def markdown_to_text_file(input_filename, output_filename):
    # Read Markdown content from the input file
    with open(input_filename, 'r', encoding='utf-8') as input_file:
        markdown_content = input_file.read()

    # Convert Markdown to HTML
    html = markdown(markdown_content)

    # Use BeautifulSoup to extract text from HTML
    text = ''.join(BeautifulSoup(html, "html.parser").findAll(text=True))

    # Write the text to the output file
    with open(output_filename, 'w', encoding='utf-8') as text_file:
        text_file.write(text)

# Usage
input_filename = 'world-southern-feel-personal-benefit.md'
output_filename = 'output.txt'
markdown_to_text_file(input_filename, output_filename)





## XML TO TXT CONVERSION

import xml.etree.ElementTree as ET
import re

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

# Usage
input_xml_filename = 'marriage-management.xml'
output_txt_filename = 'output.txt'
convert_xml_to_txt(input_xml_filename, output_txt_filename)
