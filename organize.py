import os
from pathlib import Path,PurePath
import shutil
from datetime import datetime
import sys
import logging

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
print(os.getcwdb())
down = os.chdir('/Users/thehe/Downloads')
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

    # lis = os.listdir()
    # print(lis)
    # lis1 = lis.copy()
    # for i in range(len(lis1)):
    #     if lis1[i].endswith('.pdf'):
    #         p = os.path.join(os.getcwd(), lis1[i])
    #         dst = os.path.join(os.getcwd(), "PDF_Folder", lis1[i])
    #         shutil.move(p,dst)

if __name__ == "__main__":
    if len(sys.argv)>1:
        new_file_path = sys.argv[1]
        structureDownloadFolder()
    else:
        print("Error: No file path provided.")
