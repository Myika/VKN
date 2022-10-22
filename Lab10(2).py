import os, glob
import shutil
a='/Users/llirik/Desktop/Univer/VKN/WEST'
b='/Users/llirik/Desktop/Univer'
os.mkdir(a)
os.chdir(b)
masiv=[]
for file in glob.glob("w*.*"):
    shutil.copy2(file,a)
    masiv.append(file)
print("Кількість файлів",len(masiv))
