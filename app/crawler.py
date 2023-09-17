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

from utils import save_dict_as_pickle
from pathlib import Path


def classifier(file_path):
    # Check the data type

    mime_type = magic.Magic()
    file_extension = mime_type.from_buffer(file_path.read_bytes())
    content = ""
    if file_extension.startswith("text"):
        file_extension = ".txt"
    elif file_extension.startswith("PDF"):
        file_extension = ".pdf"
    elif file_extension.startswith("Microsoft Excel"):
        file_extension = ".xlsx"
    elif file_extension.startswith("PNG"):
        file_extension = ".png"

    if file_path.suffix == ".txt":
        # Open the file to read out the content
        with open(file_path, encoding='utf-8') as f:
            content = f.read()
            f.close()
            # If the file contains the word "hello" label it as true
    else:
        # If it is not a `.txt` file the set the label to "review"
        return "review"


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

            file_path = file_dir_path / file_name
            labels[file_name] = classifier(file_path)

        # Save the label dictionary as a Pickle file
        save_dict_as_pickle(labels, script_dir_path_parent / 'results' / 'crawler_labels.pkl')
    else:
        output_dir = script_dir_path_parent / 'results'
        os.makedirs(output_dir, exist_ok=True)
        save_dict_as_pickle(labels, output_dir / 'crawler_labels.pkl')
        print("Please place the files in the corresponding folder")



if __name__ == "__main__":
    main()
