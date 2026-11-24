from pathlib import Path

import kagglehub
import pandas as pd

from kaggle_experiments.schemas import RawAppointmentsSchema

file_path = "KaggleV2-May-2016.csv"
target_dir = Path("data/raw/joniarroba/noshowappointments")

def main() -> None:
    print("Hello")
    dataset_path = kagglehub.dataset_download("joniarroba/noshowappointments", output_dir = str(target_dir))
    raw_df = pd.read_csv(Path(dataset_path) / file_path)
    raw_df.info()
    df = RawAppointmentsSchema.validate(raw_df)
    df.info()
    print(f"First 5 records: {df.head()}")