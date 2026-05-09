import sys
import time
from pathlib import Path, PurePath
import logging
import os
import platformdirs 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import organizes_download_dir

logging.basicConfig(level=logging.WARNING)

class WATCH(FileSystemEventHandler):

    def on_any_event(self, event):
        logging.warning(f" {event.event_type} {event.src_path}.")
        
    
path = platformdirs.user_downloads_dir()

if __name__ == "__main__":
    observer = Observer()
    event_class = WATCH()
    observer.schedule(event_class, path, recursive=True)
    observer.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
        observer.stop()
        observer.join()  #Wait until the observer thread fully stops before exiting