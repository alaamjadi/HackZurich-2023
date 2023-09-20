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
### Use the magic library for classifying files by their signatures
#import magic
import pandas as pd 
import numpy as np 


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
    from PIL import Image, ImageEnhance, ImageFilter
    import pytesseract
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

def evaluator(actual, prediction, file_dir_path):
    official_score = 0    
    print()
    print()
    print()
    print(actual)
    print()
    print(prediction)
    for file_name in os.listdir(str(file_dir_path)+"/results"):
        gt = actual.iloc[file_name]
        pred = predict.iloc[file_name]

        if actual=="TRUE" and pred=="TRUE":
            official_score += 20
        elif actual=="TRUE" and pred=="FALSE":
            official_score -= 20
        elif actual=="TRUE" and pred=="REVIEW":
            official_score += 10
        elif actual=="FALSE" and pred=="TRUE":
            official_score -= 2
        elif actual=="FALSE" and pred=="FALSE":
            official_score += 2
        elif actual=="FALSE" and pred=="REVIEw":
            official_score -= 1
    return official_score


def accuracy(X, y, W):
    yes, no = 0, 0
    testRows = X.shape[0]

    for i in range(testRows):
        fv = X[i]                
        actual = y[i]
        prediction = predict(fv, W)

        if actual == prediction:
            yes += 1
        else:
            no += 1
    score = (yes/(yes+no)) * 100 
    return score, no





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

    gt = pd.read_csv(str(script_dir_path_parent) +"/results/labels.csv", header=0)
    pred = pd.read_pickle(str(script_dir_path_parent) +"/results/crawler_labels.pkl")
    pred = pd.DataFrame.from_dict(pred, orient='index')
    print(pred)
    print(evaluator(gt, pred,script_dir_path_parent))
    print(accuracy(gt, pred))


if __name__ == "__main__":
    main()
