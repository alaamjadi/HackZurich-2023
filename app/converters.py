import io

import PyPDF2
import extract_msg
import pytesseract as pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import speech_recognition as sr
import re
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
from pydub import AudioSegment
import sqlite3
from io import BytesIO
import pandas as pd

image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']

from docx import Document

def read_docx(file_path):
    doc = Document(file_path)
    full_text = []

    for para in doc.paragraphs:
        full_text.append(para.text)

    return '\n'.join(full_text)

def pdf_to_text(pdf_path):
    text_content = ""

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfFileReader(file)

        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text_content += page.extractText()

    return text_content

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
            return "error"
    except Exception as e:
        return "error"


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


def csv_to_xlsx_pd(file_name):
    df = pd.read_csv(file_name, on_bad_lines='skip')
    output = BytesIO()
    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name='data', index=False)
    output.seek(0)
    return pd.ExcelFile(output)


def loadXlsx(file_name):
    xl = pd.ExcelFile(file_name)
    return xl


def getXlxsFromDB(file_name):
    conn = sqlite3.connect(file_name)

    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Loop through each table and export data to separate Excel sheets
    for table in tables:
        table_name = table[0]
        output = BytesIO()
        # Export data to an Excel sheet in memory sheets
        df = pd.read_sql_query(f"SELECT * FROM {table_name};", conn)
        # print(table_name)
        if table_name != 'sqlite_sequence':
            output = BytesIO()
            with pd.ExcelWriter(output, engine='openpyxl') as writer:
                df.to_excel(writer, sheet_name='data', index=False)
            output.seek(0)
            conn.close()
            return pd.ExcelFile(output)
        else:
            print(table_name)


def parse(instance, type='xlsx'):
    sheet_list = instance.sheet_names
    concatenated_df = pd.DataFrame()

    for sheet_name in sheet_list:
        # Read each sheet into a DataFrame
        df = pd.read_excel(instance, sheet_name=sheet_name, engine='openpyxl')

        # Stack the DataFrame one below the other
        concatenated_df = pd.concat([concatenated_df, df], ignore_index=True)
        if type == 'db':
            concatenated_df.dropna(inplace=True)

    csv_data = concatenated_df.to_csv(header=False, index=False)

    return csv_data

