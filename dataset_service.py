import pandas as pd
import os


DATASET_PATH = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../dataset")
)


def load_dataset(filename):
    file_path = os.path.join(DATASET_PATH, filename)

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Dataset file not found: {file_path}"
        )

    return pd.read_csv(file_path)


def get_all_dataset_info():
    files = [
        "users_data.csv",
        "peerness_values.csv",
        "Aggressive_All.csv",
        "Non_Aggressive_All.csv",
        "Communication_Data_Among_Users.csv",
        "CB_Labels.csv"
    ]

    result = {}

    for filename in files:
        df = load_dataset(filename)

        result[filename] = {
            "rows": len(df),
            "columns": df.columns.tolist()
        }

    return result