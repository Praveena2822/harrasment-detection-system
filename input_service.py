import pandas as pd
from pathlib import Path


DATASET_DIR = Path(__file__).resolve().parent.parent.parent / "dataset"


class InputService:

    def __init__(self):
        communication_file = DATASET_DIR / "Communication_Data_Among_Users.csv"
        labels_file = DATASET_DIR / "CB_Labels.csv"

        self.communication_df = pd.read_csv(communication_file)
        self.labels_df = pd.read_csv(labels_file)

    def get_user_context(self, user1_id, user2_id, message):

        # Find communication between the two users
        communication = self.communication_df[
            (self.communication_df["User1 ID"] == user1_id) &
            (self.communication_df["User2 ID"] == user2_id)
        ]

        # Find summary information for the user pair
        labels = self.labels_df[
            (self.labels_df["User1 ID"] == user1_id) &
            (self.labels_df["User2 ID"] == user2_id)
        ]

        if labels.empty:
            return {
                "found": False,
                "message": "No existing interaction data found for this user pair."
            }

        label_record = labels.iloc[0]

        return {
            "found": True,

            "message": message,

            "user1_id": user1_id,
            "user2_id": user2_id,

            "total_messages": int(
                label_record["Total_messages"]
            ),

            "aggressive_count": int(
                label_record["Aggressive_Count"]
            ),

            "intent_to_harm": float(
                label_record["Intent_to_Harm"]
            ),

            "peerness": float(
                label_record["Peerness"]
            ),

            "cyberbullying_label": int(
                label_record["CB_Label"]
            ),

            "matched_interactions": len(communication)
        }