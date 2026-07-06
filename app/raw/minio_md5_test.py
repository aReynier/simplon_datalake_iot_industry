import hashlib
import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def calculate_minio_md5():
    s3 = boto3.client('s3',
            endpoint_url='http://localhost:9000',
            aws_access_key_id=os.getenv("MINIO_ROOT_USER"),
            aws_secret_access_key=os.getenv("MINIO_ROOT_PASSWORD"))
    
    object = s3.get_object(Bucket='raw', Key='production_lines/lineA/LineA_Stable_10K.csv')

    file_bytes = object['Body'].read()

    minio_md5 = hashlib.md5(file_bytes).hexdigest()

    return minio_md5


if __name__ == "__main__":
    calculate_minio_md5()