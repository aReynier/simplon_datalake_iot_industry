import sys
import boto3
import os
from dotenv import load_dotenv

load_dotenv()


def upload_csv(file_name, line_name):
    s3 = boto3.client('s3',
                endpoint_url='http://localhost:9000',
                aws_access_key_id=os.getenv("MINIO_ROOT_USER"),
                aws_secret_access_key=os.getenv("MINIO_ROOT_PASSWORD"))

    # Simple CSV upload in bucket raw
    # next goal: partitioning as year/month/line on raw
    s3.upload_file(f"data_input/{file_name}.csv", "raw", f"/production_lines/line{line_name}/{file_name}.csv")

    response = s3.list_objects(Bucket='raw')
    for obj in response.get('Contents', []):
        print(obj['Key'])


def ingest_data(file_name, line_name):
    upload_csv(file_name, line_name)


if __name__ == "__main__":
    ingest_data()