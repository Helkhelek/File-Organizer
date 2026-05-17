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

download_directory_path = os.chdir(downloads)

# class Org():

#     def __init__(self, filename, filepath):
#         self.filename = filename
#         self.filepath = filepath

#     # todo

def Org(filename, filepath):
    pass