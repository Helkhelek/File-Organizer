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

dic_of_dir_extension ={ documents : [
    ".pdf",
    ".doc",
    ".docx",
    ".txt",
    ".rtf",
    ".odt",
    ".xls",
    ".xlsx",
    ".ppt",
    ".pptx",
    ".csv",
    ".json",
    ".xml",
    ".yaml",
    ".yml",
    ".md"
],desktop : [
    ".exe",
    ".lnk",
    ".url",
    ".bat",
    ".msi",
    ".app",
    ".desktop"
],
music : [
    ".mp3",
    ".wav",
    ".aac",
    ".flac",
    ".ogg",
    ".wma",
    ".m4a",
    ".aiff",
    ".alac"
],
video : [
    ".mp4",
    ".mkv",
    ".avi",
    ".mov",
    ".wmv",
    ".flv",
    ".webm",
    ".mpeg",
    ".mpg",
    ".3gp"
],
pictures : [
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".webp",
    ".bmp",
    ".tiff",
    ".tif",
    ".svg",
    ".ico",
    ".heic",
    ".raw",
    ".psd",
    ".ai",
    ".avif",
    ".cr2",
    ".cr3",
    ".nef",
    ".arw",
    ".dng"
]}

def Org(filename, filepath):
    for key,value in dic_of_dir_extension.items():
        for v in value:
            if filename.endswith(v):
                shutil.move(filepath, dst=key)
                break
