import pandas as pd

def prepare_data(file_path):
    df = pd.read_csv(file_path)

    # Clean data
    df.drop_duplicates(inplace=True)
    df.fillna({"Certificate": "Not Rated"}, inplace=True)

    # Save cleaned data for debugging or reuse
    df.to_csv("static/cleaned_imdb_top_1000.csv", index=False)
    return df
