import os, glob, shutil
o = -1
while o < 0:
    for f in glob.glob(r"C:\Users\cryto\Downloads\*.pdf"):
        shutil.move(f, r"C:\Users\cryto\Documents\Moje")

    for f in glob.glob(r"C:\Users\cryto\Downloads\*.jpg"):
        shutil.move(f, r"C:\Users\cryto\Pictures")

    for f in glob.glob(r"C:\Users\cryto\Downloads\*.png"):
        shutil.move(f, r"C:\Users\cryto\Pictures")

    for f in glob.glob(r"C:\Users\cryto\Downloads\*.mp4"):
        shutil.move(f, r"C:\Users\cryto\Videos")

    for f in glob.glob(r"C:\Users\cryto\Downloads\*.mp3"):
        shutil.move(f, r"C:\Users\cryto\Music")
        
    for f in glob.glob(r"C:\Users\cryto\Downloads\*.ppt"):
        shutil.move(f, r"C:\Users\cryto\Videos")

    for f in glob.glob(r"C:\Users\cryto\Downloads\*.doc"):
        shutil.move(f, r"C:\Users\cryto\Videos")

    for f in glob.glob(r"C:\Users\cryto\Downloads\*.mobi"):
        shutil.move(f, r"C:\Users\cryto\E-books")

    for f in glob.glob(r"C:\Users\cryto\Downloads\*.epub"):
        shutil.move(f, r"C:\Users\cryto\E-books")