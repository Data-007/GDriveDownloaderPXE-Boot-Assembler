import hashlib

def download_file(drive, file_id, dest_path):
    """
    Downloads a file from Google Drive to a specified local path.
    
    Parameters:
    - drive: Authenticated GoogleDrive instance.
    - file_id: ID of the file to download.
    - dest_path: Local path to save the downloaded file.
    """
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(dest_path)

def verify_checksum(file_path, expected_checksum):
    """
    Verifies the SHA-256 checksum of a downloaded file.
    
    Parameters:
    - file_path: Path to the local file to verify.
    - expected_checksum: The expected checksum value to compare against.
    
    Returns:
    - True if the checksum matches, False otherwise.
    """
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest() == expected_checksum
