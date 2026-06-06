import os
import shutil

os.chdir(os.path.expanduser("~/Documents/Python Projects"))

extensions = {
    "images": [".jpg", ".jpeg", ".png", ".gif"],
    "videos": [".mp4", ".mkv"],
    "music": [".mp3", ".wav"],
    "zip": [".zip", ".rar"],
    "documents": [".pdf", ".docx", ".txt"],
    "setup": [".exe", ".msi"],
    "programs": [".py", ".js", ".html", ".css", ".java", ".cpp"]
}

for folder in list(extensions.keys()) + ["others"]:
    os.makedirs(folder, exist_ok=True)

def sorting(file):
    for key, exts in extensions.items():
        for ext in exts:
            if file.lower().endswith(ext):
                return key

files = os.listdir()

for file in files:
    if not os.path.isfile(file):
        continue
    dist = sorting(file)
    if dist:
        try:
            shutil.move(file, dist)
        except shutil.Error as e:
            print(e)
    else:
        try:
            shutil.move(file, "others")
        except shutil.Error as e:
            print(e)