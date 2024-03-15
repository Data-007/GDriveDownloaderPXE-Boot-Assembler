import tkinter as tk
from tkinter import scrolledtext
from threading import Thread

def start_process_thread(gauth):
    """
    Starts the file processing in a separate thread to keep the GUI responsive.
    
    Parameters:
    - gauth: Authenticated GoogleAuth instance.
    """
    thread = Thread(target=start_process, args=(gauth,))
    thread.start()

def start_process(gauth):
    """
    Main process that lists, downloads, and verifies .iso files.
    
    Parameters:
    - gauth: Authenticated GoogleAuth instance.
    """
    drive = GoogleDrive(gauth)
    for file_id, title in list_iso_files(gauth):
        dest_path = f'/path/to/download/{title}'  # Define your destination path
        download_file(drive, file_id, dest_path)
        # Replace 'expected_checksum_here' with actual checksum retrieval logic
        if verify_checksum(dest_path, 'expected_checksum_here'):
            log(f'Checksum verified for {title}')
        else:
            log(f'Checksum failed for {title}')

def log(message):
    """
    Logs a message to the GUI's text area.
    
    Parameters:
    - message: The message to log.
    """
    text_area.configure(state='normal')
    text_area.insert(tk.END, message + "\n")
    text_area.configure(state='disabled')

# Setting up the GUI
app = tk.Tk()
app.title("ISO Sync and Verify")

frame = tk.Frame(app)
frame.pack(padx=10, pady=10)

start_button = tk.Button(frame, text="Start Process", command=lambda: start_process_thread(gauth))
start_button.pack(side=tk.TOP, pady=5)

text_area = scrolledtext.ScrolledText(frame, wrap=tk.WORD, state='disabled')
text_area.pack(padx=10, pady=10)

app.mainloop()
