import pandas as pd
from pathlib import Path


DATASET_DIR = Path(__file__).resolve().parent.parent.parent / "dataset"


def prepare_dataset():

    communication_file = DATASET_DIR / "Communication_Data_Among_Users.csv"
    labels_file = DATASET_DIR / "CB_Labels.csv"

    # Load communication data
    communication_df = pd.read_csv(communication_file)

    # Load user-pair labels
    labels_df = pd.read_csv(labels_file)

    # Rename columns
    communication_df = communication_df.rename(columns={
        "User1 ID": "user1_id",
        "User2 ID": "user2_id",
        "Message": "message",
        "Label": "message_label"
    })

    labels_df = labels_df.rename(columns={
        "User1 ID": "user1_id",
        "User2 ID": "user2_id",
        "Total_messages": "total_messages",
        "Aggressive_Count": "aggressive_count",
        "Intent_to_Harm": "intent_to_harm",
        "Peerness": "peerness",
        "CB_Label": "cyberbullying_label"
    })

    # Combine both datasets using user pair
    merged_df = communication_df.merge(
        labels_df,
        on=["user1_id", "user2_id"],
        how="left"
    )

    return merged_df


if __name__ == "__main__":

    print("Starting dataset preprocessing...")

    df = prepare_dataset()

    print("\nPreprocessing completed successfully!")

    print("Total records:", len(df))

    print("\nFinal columns:")
    print(list(df.columns))

    print("\nSample processed records:")
    print(df.head(5).to_string(index=False))