from pathlib import Path
import pandas as pd
from prefect_gcp.cloud_storage import GcsBucket
from prefect import flow, task
from prefect_gcp import GcpCredentials

@task(retries=3)
def extract_from_gcs(color: str, year: int, month:int) -> Path:
    """Download data from GCS"""
    print("-------------")
    gcs_path = f"{color}/{color}_tripdata_{year}-{month:02}.parquet"
    gcp_cloud_storage_bucket_block = GcsBucket.load("ny-taxi-gcs")
    gcp_cloud_storage_bucket_block.get_directory(from_path=gcs_path, local_path=f"../") 
    return Path(f"../{gcs_path}")

@task()
def transform(path: Path) -> Path:
    """Data cleaning"""
    df = pd.read_parquet(path)
    print(f"pre: missing passenger count: {df['passenger_count'].isna().sum()}")
    df["passenger_count"].fillna(0, inplace=True)
    print(f"post: missing passenger count: {df['passenger_count'].isna().sum()}")
    return df

def write_bq(df: pd.DataFrame) -> None:
    """Write dataframe to BigQuery"""
    gcp_credentials_block = GcpCredentials.load("ny-taxi-gcp-credentials")


    df.to_gbq(destination_table="trips_data_all.rides",
              project_id="fourth-library-393410", 
              credentials=gcp_credentials_block.get_credentials_from_service_account(),
              chunksize=500000,
              if_exists="append")

@flow()
def etl_gcs_to_bq():
    """Main ETL flow to load data to BigQuery"""
    color = "yellow"
    year = 2021
    month = 1
    # print(color)

    path = extract_from_gcs(color,year,month)
    
    # print(path)

    df = transform(path)

    write_bq(df)

if __name__ == "__main__":
    etl_gcs_to_bq()
