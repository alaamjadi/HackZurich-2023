import pickle
import pandas as pd
from pathlib import Path

# Define the path to the pickle file and where you want to save the CSV
pickle_path = Path('crawler_labels.pkl')
csv_path = Path('crawler_labels.pkl.csv')

# Load the dictionary back from the pickle file
with open(pickle_path, 'rb') as handle:
    loaded_labels = pickle.load(handle)

# Convert the dictionary to a DataFrame
df = pd.DataFrame(list(loaded_labels.items()), columns=['File Name', 'Label'])

# Save the DataFrame to CSV
df.to_csv(csv_path, index=False)
