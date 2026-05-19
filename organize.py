import os
import platformdirs
import shutil


# Pictures, Gallery, Video, Music, Downloads, Documents, Desktop, Home, One Drive. 


documents = platformdirs.user_documents_dir()
desktop = platformdirs.user_desktop_dir()
music = platformdirs.user_music_dir()
video = platformdirs.user_videos_dir()
downloads = platformdirs.user_downloads_dir()
pictures = platformdirs.user_pictures_dir()


# class Org():

#     def __init__(self, filename, filepath):
#         self.filename = filename
#         self.filepath = filepath

#     # todo

list_of_dirs_path = [documents, desktop, music, video, pictures]
list_of_file_extension = [ ".jpg",".jpeg", ".png",".gif",".webp",".bmp",".tiff",".tif",".svg",".ico",".heic",".raw",".psd",".ai",".avif",".cr2",".cr3",".nef",".arw",".dng"]

def Org(filename, filepath):
    for i in list_of_file_extension:
        if filename.endswith(i):
            shutil.move(filepath, dst=pictures)
            break


# def loopOnindividualDir():
#     pass

Org("download.jpg","C:/Users/thehe/Downloads/download.jpg")