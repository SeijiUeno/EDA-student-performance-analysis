import os
import pandas as pd

def save_dataframe(df, directory, filename, index=False):
    os.makedirs(directory, exist_ok=True)
    filepath = os.path.join(directory, filename)
    df.to_csv(filepath, index=index)
    print(f"\033[92m ✅ Success - DataFrame saved at: {filepath} ✔\033[0m")