from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def login():
    gauth = GoogleAuth()
    # Creates local webserver and auto handles authentication.
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    return drive

drive = login()
