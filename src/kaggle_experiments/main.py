import kagglehub, pandas as pd
from kagglehub import KaggleDatasetAdapter
from pathlib import Path

file_path = "KaggleV2-May-2016.csv"
target_dir = Path("data/raw/joniarroba/noshowappointments")

def main() -> None:
    print("Hello")
    dataset_path = kagglehub.dataset_download("joniarroba/noshowappointments", output_dir = str(target_dir))
    df = pd.read_csv(Path(dataset_path) / file_path)
    df.info()
    #print(df.isna().sort_index(1))
    #print(f"Dataframe info: {df.info()}")
    #print(f"Has any: {df.isna()}")
    print(f"First 5 records: {df.head()}")
    #print(f"First 10 sorted: {df.sort_index(), df.head()}")