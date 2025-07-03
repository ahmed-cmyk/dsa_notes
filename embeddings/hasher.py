import hashlib
from pathlib import Path


class Hasher():
    def __init__(self, folders):
        self.folders = folders

    def file_hash(self, path, algo='sha256', chunk_size=8192):
        h = hashlib.new(algo)
        with open(path, 'rb') as f:
            while chunk := f.read(chunk_size):
                h.update(chunk)
        return h.hexdigest()

    def hash_folder(self, folder, algo='sha256'):
        folder_path = Path(folder)
        hashes = []

        for file_path in folder_path.rglob('*'):
            if file_path.is_file():
                file_hash_str = self.file_hash(file_path, algo)
                hashes.append((str(file_path), file_hash_str))

        return hashes

    def start_hashing(self):
        hashes = []

        for folder in self.folders:
            hashes += self.hash_folder(folder)

        return hashes
