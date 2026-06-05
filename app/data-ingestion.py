import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def inject_data():
    s3 = boto3.client('s3',
                endpoint_url='http://localhost:9000',
                aws_access_key_id=os.getenv("MINIO_ROOT_USER"),
                aws_secret_access_key=os.getenv("MINIO_ROOT_PASSWORD"))

    # Simple CSV upload in bucket raw
    # next goal: partitioning as year/month/line on raw
    s3.upload_file("data_input/LineA_Stable_10K.csv", "raw", "/production_lines/lineA/LineA_Stable_10K.csv")
    s3.upload_file("data_input/LineA_Stable_10K.csv", "raw", "/production_lines/lineB/LineB_Flux.csv")
    s3.upload_file("data_input/LineA_Stable_10K.csv", "raw", "/production_lines/lineC/LineC_Turbulent.csv")
    s3.upload_file("data_input/LineA_Stable_10K.csv", "raw", "/production_lines/lineD/LineD_SpikeControl.csv")
    s3.upload_file("data_input/LineA_Stable_10K.csv", "raw", "/production_lines/lineE/LineE_SmoothRun.csv")

    response = s3.list_objects(Bucket='raw')
    for obj in response.get('Contents', []):
        print(obj['Key'])

def main():
    inject_data()


if __name__ == "__main__":
    main()