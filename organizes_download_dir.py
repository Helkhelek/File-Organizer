import os
from pathlib import Path,PurePath
import shutil
from datetime import datetime
import sys
import logging
import platformdirs 
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEvent, FileSystemEventHandler
import subprocess

# File Organizer

listOfDirectories = {
    "Picture_Folder": ['.jpeg', '.jpg', '.gif', '.png', ".webp", '.svg'],
    "Video_Folder": ['wmv', '.mov', '.mp4','.mpg', '.mpeg', '.mkv'],
    "Zip_Folder": ['.iso', '.tar', '.gz', '.rz', '.7z','.dmg', 'rar', '.zip'],
    "Music_Folder": ['.mp3', '.msv','.wav', '.wma'],
    "PDF_Folder": ['.pdf'],
    "Applications" : ['.exe']
}

print(os.getcwd())
down = os.chdir(platformdirs.user_downloads_path())
print(os.getcwd())

lisOFilesAndFolderInDownload = os.listdir() #we are currently in download folder
lis1 = lisOFilesAndFolderInDownload.copy()

def structureDownloadFolder():
        for key, value in listOfDirectories.items():
            try:
                os.mkdir(key)
                for i in lis1:
                    for v in value:
                        if i.endswith(v):
                            p = os.path.join(os.getcwd(), i)
                            des = os.path.join(os.getcwd(), key , i)
                            shutil.move(p, dst=des)
            except FileExistsError:
                for i in lis1:
                    for v in value:
                        if i.endswith(v):
                            p = os.path.join(os.getcwd(), i)
                            des = os.path.join(os.getcwd(), key , i)
                            shutil.move(p, dst=des)

structureDownloadFolder()
