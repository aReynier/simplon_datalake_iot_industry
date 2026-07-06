import hashlib

def calculate_local_md5(local_file_path):

    with open(local_file_path, 'rb') as f:
        file_content = f.read()
        local_md5 = hashlib.md5(file_content).hexdigest()

    return local_md5


if __name__ == "__main__":
    calculate_local_md5()