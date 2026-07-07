import sys
import boto3
import os
from dotenv import load_dotenv

load_dotenv()


def upload_csv(production_line, year, month):
    s3 = boto3.client('s3',
                # Find a way to automatically change this
                # endpoint_url='http://localhost:9000',
                endpoint_url='http://minio:9000',
                aws_access_key_id=os.getenv("MINIO_ROOT_USER"),
                aws_secret_access_key=os.getenv("MINIO_ROOT_PASSWORD"))
    
    #See if it's not better to change for an online path instead of local path
    local_path = f"data_input/{production_line['name']}.csv"
    bucket_name = "raw"
    target_path = f"/year={year}/month={month}/line={production_line['id']}/{production_line['name']}.csv"

    # Simple CSV upload in bucket raw
    # next goal: partitioning as year/month/line on raw
    s3.upload_file(local_path, bucket_name, target_path)

    response = s3.list_objects(Bucket='raw')
    for obj in response.get('Contents', []):
        print(obj['Key'])


def ingest_data(production_line, year, month):
    upload_csv(production_line, year, month)


if __name__ == "__main__":
    ingest_data()