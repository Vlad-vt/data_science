from pathlib import Path

import kagglehub
import pandas as pd

from kaggle_experiments.preprocessing import prepare_appointments
from kaggle_experiments.schemas import RawAppointmentsSchema

FILE_PATH = "KaggleV2-May-2016.csv"
RAW_DIR = Path("data/raw/joniarroba/noshowappointments")
PROCESSED_PATH = Path("data/processed/appointments.parquet")

def main() -> None:
    print("Hello")
    dataset_path = kagglehub.dataset_download("joniarroba/noshowappointments", output_dir = str(RAW_DIR))
    raw_df = pd.read_csv(Path(dataset_path) / FILE_PATH)
    validated_df = RawAppointmentsSchema.validate(raw_df)
    clean_df = prepare_appointments(validated_df)
    PROCESSED_PATH.parent.mkdir(parents = True, exist_ok = True)
    clean_df.to_parquet(PROCESSED_PATH, index = False)
    print(f"Сохранено строк: {len(clean_df)}, колонок: {clean_df.shape[1]}")
    print(f"Доля неявок (target=1): {clean_df['target'].mean():.4f}")
    print(
        clean_df[
            ["lead_time_days", "prev_appointments", "prev_noshows", "target"]
        ].head()
    )
    print(f"First 5 records: {clean_df.head()}")