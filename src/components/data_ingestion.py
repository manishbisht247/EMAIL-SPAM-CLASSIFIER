import os
import pandas as pd
from src.utils.email_parser import extract_email_body

def load_spamassassin_data(base_path):
    data = []

    label_map = {
        "spam": 1,
        "easy_ham": 0,
        "hard_ham": 0
    }

    for folder, label in label_map.items():
        folder_path = os.path.join(base_path, folder)

        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)

            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="latin-1") as f:
                    text = extract_email_body(file_path)

                data.append({
                    "text": text,
                    "label": label
                })

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = load_spamassassin_data("data/raw/spamassassin")
    print(df.sample(6))
    print(df["label"].value_counts())
