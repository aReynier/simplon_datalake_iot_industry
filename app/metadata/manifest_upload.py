import sys
import boto3
import os
from dotenv import load_dotenv
from pathlib import Path
import json

load_dotenv()


def upload_manifest():
    s3 = boto3.client('s3',
            # Find a way to automatically change this
            # endpoint_url='http://localhost:9000',
            endpoint_url='http://localhost:9000',
            aws_access_key_id=os.getenv("MINIO_ROOT_USER"),
            aws_secret_access_key=os.getenv("MINIO_ROOT_PASSWORD"))
    

    buckets = ["raw", "staging", "curated", "archive"]

    for bucket in buckets:
        local_path = f"metadata/{bucket}/openmetadata_storage_manifest.json"
        target_path = "openmetadata.json"

        s3.upload_file(local_path, bucket, target_path)


if __name__ == "__main__":
    upload_manifest()