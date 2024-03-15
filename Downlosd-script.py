import hashlib

def download_file(drive, file_id, dest_path):
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(dest_path)

def verify_checksum(file_path, expected_checksum):
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest() == expected_checksum
