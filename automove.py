import os
import shutil

downloads = "/home/michaelexe/Downloads"
pictures = "/home/michaelexe/Pictures"
videos = "/home/michaelexe/Videos"

os.chdir(downloads)

for files in os.listdir():
	file_name, file_ext = os.path.splitext(files)

	if file_ext == ".jpg" or file_ext == ".jpeg" or file_ext == ".png":
		shutil.move(files, pictures)