from pydrive.drive import GoogleDrive

def list_iso_files(gauth, folder_id='root'):
    """
    Lists all .iso files in a specified Google Drive folder.
    
    Parameters:
    - gauth: Authenticated GoogleAuth instance.
    - folder_id: ID of the Google Drive folder to search (default is 'root').
    
    Returns:
    - List of tuples containing file IDs and titles of .iso files.
    """
    drive = GoogleDrive(gauth)
    query = f"'{folder_id}' in parents and trashed=false and mimeType='application/octet-stream'"
    file_list = drive.ListFile({'q': query}).GetList()
    return [(file['id'], file['title']) for file in file_list if file['title'].endswith('.iso')]
