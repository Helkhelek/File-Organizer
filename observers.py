import sys
import time
from pathlib import Path, PurePath
import logging
import queue    
from queue import Queue
import os
import platformdirs 
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import organizes_download_dir
from organize import Org

logging.basicConfig(level=logging.WARNING)


class WATCH(FileSystemEventHandler):
       
    def on_created(self, event):
            time.sleep(2)
            logging.warning(f" {event.event_type} {event.src_path}.")
            filename = os.path.basename(event.src_path)
            Org(filename, event.src_path)
      

        

downloads = platformdirs.user_downloads_dir()  
    
observer = Observer()
event_class = WATCH()
observer.schedule(event_class, downloads, recursive=True)
observer.start()


try:
    while True:
        time.sleep(2)
except KeyboardInterrupt:
        observer.stop()    
        observer.join()  #Wait until the observer thread fully stops before exiting