import hashlib
import subprocess
import time
import os

def hash_file(file_path, algorithm="sha256", buffer_size=65536):
    hasher = hashlib.new(algorithm)

    with open(file_path, "rb") as file:
        buffer = file.read(buffer_size)

        while len(buffer) > 0:
            hasher.update(buffer)
            buffer = file.read(buffer_size)
        
    # Return the hexadecimal representation of the hash
    return hasher.hexdigest()

def run_in_new_console(file_path):
    subprocess.Popen(["start", "cmd", "/k", f"python {file_path}"], shell=True)

if __name__ == "__main__":
    file_path = input("Enter the file path: ")

    # Validate file path
    if not os.path.isfile(file_path):
        print("Invalid file path. Please provide a valid file path.")
        exit()

    hash_value = hash_file(file_path)
    
    try:
        while True:
            time.sleep(1)
            tmp = hash_file(file_path)

            if hash_value != tmp:
                hash_value = tmp
                print(f"File changed. New hash: {hash_value}")
                run_in_new_console(file_path)
    except KeyboardInterrupt:
        print("Program Exiting")
    print(hash_value)
