import hashlib
from pathlib import Path

def file_hash(path, algo='sha256', chunk_size=8192):
    h = hashlib.new(algo)
    with open(path, 'rb') as f:
        while chunk := f.read(chunk_size):
            h.update(chunk)
    return h.hexdigest()

def hash_folder(folder, algo='sha256'):
    folder_path = Path(folder)
    hashes = []

    for file_path in folder_path.rglob('*'):
        if file_path.is_file():
            file_hash_str = file_hash(file_path, algo)
            hashes.append(file_hash_str)

    return hashes

def start_hashing():
    hashes = []

    for folder in ['./algorithms', './data_structures']:
        hashes += hash_folder(folder)

    return hashes
