import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
import subprocess
import os
import time

DOWNLOAD_FOLDER = "C:/Users/thehe/Downloads"

SCRIPT_TO_RUN = "C:/Users/thehe/Desktop/File Organizer/organize.py"

class NewDownloadHandler(FileSystemEventHandler):

    def run_script(self, new_file_path):
        try:
            subprocess.run(["Python", SCRIPT_TO_RUN, new_file_path], check=True)
            print(f"Successfully ran processing script for {new_file_path}")
        
        except subprocess.CalledProcessError as e:
            print(f"Error in running scrept : {e}")
        except FileNotFoundError:
            print(f"Error: The script '{SCRIPT_TO_RUN}' was not found.")

    def on_created(self, event):
        if not event.is_directory:
            print(f"Detected new file :  {event.src_path}")
            time.sleep(1)
            self.run_script(event.src_path)


if __name__ == "__main__":
    
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    path = DOWNLOAD_FOLDER
    event_handler = NewDownloadHandler()

    observer = Observer()
    observer.schedule(event_handler, path, recursive= False)
    observer.start()

    print(f"Monitoring folder : {path}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    