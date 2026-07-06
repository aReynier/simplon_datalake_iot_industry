import hashlib

# def calculate_local_md5(file_name):
    # hash_md5 = hashlib.md5()
def calculate_local_md5():

    with open(f"data_input/LineA_Stable_10K.csv", 'rb') as f:
        file_content = f.read()
        local_md5 = hashlib.md5(file_content).hexdigest()

    return local_md5


if __name__ == "__main__":
    calculate_local_md5()