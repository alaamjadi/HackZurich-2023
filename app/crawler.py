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
import magic

from converters import *
from predict import predict_file_content
from utils import save_dict_as_pickle
from pathlib import Path


def classifier(file_path):
    # Check the data type

    mime_type = magic.Magic()
    file_type_description = mime_type.from_buffer(file_path.read_bytes())
    print(file_type_description)
    if "ASCII text" or "Unicode text" or "source" or "Generic INItialization" or "RSA" in file_type_description:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            content = re.sub('<.*?>', '', content)
            content = re.sub('[^a-zA-Z0-9 \n]', '', content)
            return predict_file_content(content)
    elif "Audio file" in file_type_description:
        return predict_file_content(convert_mp3_to_text(file_path))
    elif "JPEG image" in file_type_description:
        return predict_file_content(ocr_image(file_path))
    elif "PNG image" in file_type_description:
        return predict_file_content(ocr_image(file_path))
    elif "PDF document" in file_type_description:
        return predict_file_content(pdf_to_text(file_path))
    elif "Microsoft Word" in file_type_description:
        return predict_file_content(read_docx(file_path))
    elif "Microsoft Excel" in file_type_description:
        return predict_file_content(parse(loadXlsx(file_path)))
    elif "SQLite 3.x database" in file_type_description:
        return predict_file_content(parse(getXlxsFromDB(file_path)))
    elif "CSV ASCII text" in file_type_description:
        return predict_file_content(parse(csv_to_xlsx_pd(file_path)))
    # elif "Zip archive" in file_type_description:
    #     return ArchiveFileHandler()
    elif "HTML document" in file_type_description:
        return predict_file_content(extract_text_from_html(file_path))
    else:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            content = re.sub('<.*?>', '', content)
            content = re.sub('[^a-zA-Z0-9 \n]', '', content)
            return predict_file_content(content)


def main():
    # Get the path of the directory where this script is in
    script_dir_path_parent = Path(os.path.realpath(__file__)).parents[1]
    # Get the path containing the files that we want to label
    file_dir_path = script_dir_path_parent / "files"
    labels = {}
    if os.path.exists(file_dir_path):
        # Initialize the label dictionary

        # Loop over all items in the file directory
        for file_name in os.listdir(file_dir_path):
            if isinstance(file_name, bytes):
                file_name = file_name.decode('utf-8')
            # print(file_name)
            file_path = file_dir_path / file_name
            labels[file_name] = classifier(file_path)
            print(labels[file_name])

        # Save the label dictionary as a Pickle file
        save_dict_as_pickle(labels, script_dir_path_parent / 'results' / 'crawler_labels.pkl')
    else:
        output_dir = script_dir_path_parent / 'results'
        os.makedirs(output_dir, exist_ok=True)
        save_dict_as_pickle(labels, output_dir / 'crawler_labels.pkl')
        print("Please place the files in the corresponding folder")


if __name__ == "__main__":
    main()
