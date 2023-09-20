import os
from pathlib import Path
import pickle
import re
from bs4 import BeautifulSoup

def save_dict_as_pickle(labels, filename):
    with open(filename, "wb") as handle:
        pickle.dump(labels, handle, protocol=pickle.HIGHEST_PROTOCOL)

def classifier(file_path):
    content = file_handled(file_path)
    
    # Check the data type
    if file_path.suffix == '.xxx':
        # Empty file suffix?
        print('text-file')
    
    elif file_path.suffix == '.pem':
        return private_key_detected(content)
    
    elif file_path.suffix == '.pub':
        return public_key_detected(content) & bool(name_detected_pub(content)) & email_detected(content)

    elif file_path.suffix == '.py':
        return name_detected_py(content) & iban_detected(content)

    elif file_path.suffix == '.ps1':
        return name_detected_ps1(content) & iban_detected(content)
    
    elif file_path.suffix == '.html':
        content = html_to_text(content)
        return ( (name_detected_html(content) & iban_detected(content)) or (name_detected_html(content) & email_detected(content)) or (email_detected(content) & iban_detected(content)))
        
def file_handled(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read()

def name_detected_py(content):
    pattern = r'name\":\s*\"([^\"]+)\",\s*\"surname\":\s*\"([^\"]+)\"'
    return len(re.search(pattern, content).groups()) == 2 if re.search(pattern, content) else False

def name_detected_pub(content):
    pattern = r'\s([A-Za-z]+\s[A-Za-z]+);'
    return bool(re.search(pattern, content))

def name_detected_ps1(content):
    pattern = r'(?:Client|Name|client|name):\s*([A-Z][a-z]+\s[A-Z][a-z]+)'
    return bool(re.search(pattern, content))

def name_detected_html(content):
    pattern = r'^\s*(?:name|Name)\s*:\s+((?!former)[A-Z][a-z]+)\s+([A-Z][a-z]+)'
    return bool(re.search(pattern, content))

def email_detected(content):
    pattern = r'\b[A-Za-z0-9._%+-]+ *@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    return bool(re.search(pattern, content))

def private_key_detected(content):
    pattern = r'\s*(\bBEGIN\b).*(PRIVATE KEY\b)\s*'
    return bool(re.search(pattern, content))

def public_key_detected(content):
    pattern = r'ssh-[A-Za-z0-9]+ [\w/+=;]+'
    return bool(re.findall(pattern, content, re.MULTILINE))

def iban_detected(content):
    pattern = r'\b[A-Za-z]{2}\s*[0-9]{2}\s*(?:[A-Za-z0-9]+\s*)+\b'
    return bool(re.search(pattern, content))

def phone_detected(content):
    pattern = r'\b(?:\+?\d{1,4}[()\s-]*)?\d{1,3}[()\s-]*\d{1,3}[()\s-]*\d{1,4}\b'
    return True

def html_to_text(content):
    soup = BeautifulSoup(content, 'lxml')
    return soup.get_text()

def main():
    # Get the path of the directory where this script is in
    script_dir_path = Path(os.path.realpath(__file__)).parents[1]
    # Get the path containing the files that we want to label
    file_dir_path = script_dir_path / "files"

    if os.path.exists(file_dir_path):
        # Initialize the label dictionary
        labels = {}

        # Loop over all items in the file directory
        for file_name in os.listdir(file_dir_path):
            file_path = file_dir_path / file_name
            labels[file_name] = classifier(file_path)

        # Save the label dictionary as a Pickle file
        save_dict_as_pickle(labels, script_dir_path / 'results' / 'crawler_labels.pkl')
    else:
        print("Please place the files in the corresponding folder")

if __name__ == "__main__":
    main()