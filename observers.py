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

class Watch(FileSystemEventHandler):

    def on_created(self, event):
        now = time.time()
        logging.warning(f"{event.src_path} created at {now}.")
        return now

    def on_modified(self, event):
        now = time.time()
        logging.warning(f"{event.src_path} modified at {now}.")
        return now
    
    def on_any_event(self, event):
        now =time.time()
        organizes_download_dir.structureDownloadFolder()
        logging.warning(f" {event.event_type} {event.src_path}  at {now}.")
        return now
    
path = platformdirs.user_downloads_dir()
print(path)
observer = Observer()
observer.schedule(Watch(),path, recursive=True)
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
        observer.stop()
observer.join()

