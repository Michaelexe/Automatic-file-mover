import os
import shutil

downloads = "/home/michaelexe/Downloads"
pictures = "/home/michaelexe/Pictures"
videos = "/home/michaelexe/Videos"
music = "/home/michaelexe/Music"
os.chdir(downloads)

for files in os.listdir():
	file_name, file_ext = os.path.splitext(files)

	if file_ext == ".jpg" or file_ext == ".jpeg" or file_ext == ".png":
		shutil.move(files, pictures)

	if file_ext == ".mp4":
		shutil.move(files, videos)

	if file_ext == ".mp3":
		shutil.move(files, music)