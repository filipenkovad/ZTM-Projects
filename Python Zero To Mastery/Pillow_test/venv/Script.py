import sys
import os
from PIL import Image

#take 2 arguements from command line
folder = sys.argv[1]
new_folder = sys.argv[2]
#check new folder exist or not, if not, create it
if not os.path.exists(f'./{folder}/{new_folder}'):
    os.mkdir(f'./{folder}/{new_folder}')
#loop through Pokedex folder, convert images to PNG and save to new folder
for filename in os.listdir(str(sys.argv[1])):
    if filename.endswith(".jpg"):
        f,e = os.path.splitext(filename)
        outfile = f + ".png"
        if filename != outfile:
            try:
                with Image.open(f"./{folder}/{filename}") as im:
                    im.save(f"./{folder}/{new_folder}/{outfile}")
            except IOError:
                print("cannot convert", filename)


