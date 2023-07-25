from pathlib import Path
import pandas as pd
from prefect_gcp.cloud_storage import GcsBucket
from prefect import flow, task


@task
def fetch(dataset_url: str) -> pd.DataFrame:
    """get taxi data from the web and read the csv"""
    df = pd.read_csv(dataset_url)
    return df

@task
def clean(df: pd.DataFrame) -> pd.DataFrame:
    """fix dtype issues"""
    df["tpep_pickup_datetime"] = pd.to_datetime(df["tpep_pickup_datetime"])
    df["tpep_dropoff_datetime"] = pd.to_datetime(df["tpep_dropoff_datetime"])
    print(df.head(2))
    print(f"columns: {df.dtypes}")
    print(f"rows: {len(df)}")
    return df

@flow
def etl_web_to_gcs() -> None:
    """Main ETL function"""
    color = 'yellow'
    year = 2021
    month = 1
    dataset_file = f"{color}_tripdata_{year}-{month:02}"
    dataset_url = f"https://github.com/DataTalksClub/nyc-tlc-data/releases/download/{color}/{dataset_file}.csv.gz"

    df = fetch(dataset_url)
    df_clean = clean(df)

if __name__ == "__main__":
    etl_web_to_gcs()