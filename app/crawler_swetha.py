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

