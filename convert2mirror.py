import cv2
import os


#multiple image conversions

import cv2

import os,glob

from os import listdir,makedirs

from os.path import isfile,join
path = 'dataset/train_A' # Source Folder
dstpath = 'dataset/train_A_both' # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")
# Folder won't used
files = list(filter(lambda f: isfile(join(path,f)), listdir(path)))
for image in files:
    try:
        img = cv2.imread(os.path.join(path,image))
        flipHorizontal = cv2.flip(img, 0)
        dstPath = join(dstpath,image)
        cv2.imwrite(dstPath,flipHorizontal)

    except:
        print ("{} is not converted".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = cv2.imread(fil)
        flipHorizontal_image = cv2.flip(os.path.join(path,image), 0)
        cv2.imwrite(os.path.join(dstpath,fil),flipHorizontal_image)

    except:
        print('{} is not converted')
