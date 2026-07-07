import hashlib
import boto3
import os
from dotenv import load_dotenv


load_dotenv()


def verify_data_integrity(local_file_path, minio_file_key):
    if check_local_file(local_file_path) == check_minio_object(minio_file_key):
        print('check ok')
    else:
        print('chek not ok')


def check_local_file(local_file_path):

    with open(local_file_path, 'rb') as f:
        file_content = f.read()
        local_md5 = hashlib.md5(file_content).hexdigest()

    return local_md5


def check_minio_object(minio_file_key):
    s3 = boto3.client('s3',
            endpoint_url='http://localhost:9000',
            aws_access_key_id=os.getenv("MINIO_ROOT_USER"),
            aws_secret_access_key=os.getenv("MINIO_ROOT_PASSWORD"))
    
    object = s3.get_object(Bucket='raw', Key=minio_file_key)

    file_bytes = object['Body'].read()

    minio_md5 = hashlib.md5(file_bytes).hexdigest()

    return minio_md5


if __name__ == "__main__":
    verify_data_integrity()