from PIL import Image
from os import listdir, mkdir
from os.path import isfile, join, exists
# from skimage.transform import resize

mypath = input("Dans quel dossier sont les images ? ")
imageFiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) and (f.endswith("G") or f.endswith("g")) ]
target = int(input("Dimension maximum voulue (ex 1000) : "))

if not exists(join(mypath+"/resized")):
    mkdir(mypath+"/resized")

for im in imageFiles :
    im1 = Image.open(join(mypath,im))
    originalWidth, originalHeight = im1.size
    ratio = originalWidth / originalHeight
    width = target
    height = target
    if ratio > 1 :
        width = target
        height = int(width / ratio)
    else :
        height = target
        width = int(height * ratio)

    

    im2 = im1.resize((width, height), Image.ANTIALIAS) # linear interpolation in a 2x2 environment
    im2.save(join(mypath+"/resized", "".join([str(width),"x",str(height),"_",im])))
    print (im, "redimensionnée…")
print ("Travail terminé !", len(imageFiles), "images redimensionnées.")