from local_md5_test import calculate_local_md5
from minio_md5_test import calculate_minio_md5

def check_md5(local_file_path, minio_file_key):
    if calculate_local_md5(local_file_path) == calculate_minio_md5(minio_file_key):
        print('check ok')
    else:
        print('chek not ok')

if __name__ == "__main__":
    check_md5()