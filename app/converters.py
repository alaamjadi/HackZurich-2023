import io

import extract_msg
import pytesseract as pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import speech_recognition as sr
import re
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from pydub import AudioSegment

image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']


def extract_text_from_html(input_html_file):
    # Read the HTML content from the input file
    with open(input_html_file, "r", encoding="utf-8") as file:
        html_content = file.read()

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(html_content, "html.parser")

    # Get the text content from the HTML and replace newlines with spaces
    text_content = soup.get_text().replace('\n', ' ')
    return text_content


def convert_xml_to_txt(input_xml_filename):
    try:
        # Parse the XML file
        tree = ET.parse(input_xml_filename)

        # Convert the parsed XML to plain text without newlines
        notags = ET.tostring(tree.getroot(), encoding='utf-8', method='text')
        text_content = notags.decode('utf-8').replace('\n', '')  # Remove newlines

        # Remove excess whitespace (spaces, tabs, and multiple consecutive spaces)
        text_content = re.sub(r'\s+', ' ', text_content)

        return text_content

    except ET.ParseError as e:
        print(f"Error parsing XML: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")


def im2text(im):
    im = Image.open(im)
    im = im.filter(ImageFilter.MedianFilter())
    enhancer = ImageEnhance.Contrast(im)
    im = enhancer.enhance(2)
    im = im.convert('1')
    im.save("temp.jpg")
    text = pytesseract.image_to_string(Image.open('temp.jpg'))
    return text


def ocr_image(image_path):
    try:
        # Open an image
        image = Image.open(image_path)

        # Perform OCR
        text = pytesseract.image_to_string(image)

        return text
    except Exception as e:
        return str(e)


def convert_mp3_to_text(source_directory):
    try:
        # Convert MP3 to WAV
        sound = AudioSegment.from_mp3(source_directory)

        # Save WAV to in-memory BytesIO object
        buffer = io.BytesIO()
        sound.export(buffer, format="wav")
        buffer.seek(0)  # Move buffer to start position

        # Create an AudioFile object using the in-memory WAV file
        file_audio = sr.AudioFile(buffer)

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


def extract_msg_file(source_directory):
    try:
        # Create the output directory if it doesn't exist

        # Open the .msg file
        msg = extract_msg.Message(source_directory)

        # Extract the .txt file (if it exists)
        if msg.subject:
           return  msg.body.encode('utf-8')
        else:
            return ""
    except Exception as e:
        print(f"An error occurred while extracting '{source_directory}': {str(e)}")

