from styleaug import StyleAugmentor

import torch
from torchvision.transforms import ToTensor, ToPILImage
from PIL import Image
from matplotlib import pyplot as plt


# PyTorch Tensor <-> PIL Image transforms:
toTensor = ToTensor()
toPIL = ToPILImage()

# load images:
import os,glob

from os import listdir,makedirs

from os.path import isfile,join
path = 'dataset/train_A' # Source Folder
dstpath = 'dataset/train_A_augmented' # Destination Folder
try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")
# Folder won't used
files = list(filter(lambda f: isfile(join(path,f)), listdir(path)))
for image in files:
    try:
        im = Image.open('dataset/train_A/0.jpg')
        im_torch = toTensor(im).unsqueeze(0) # 1 x 3 x 256 x 256
        # create style augmentor:
        augmentor = StyleAugmentor()
        # randomize style:
        im_restyled = augmentor(im_torch)
        toPIL(im_restyled.squeeze().cpu())
    except:
        print ("{} is not converted".format(image))
for fil in glob.glob("*.jpg"):
    try:
        image = Image.open(fil)
        im_torch = toTensor(os.path.join(path,image)).unsqueeze(0)  # 1 x 3 x 256 x 256
        # create style augmentor:
        augmentor = StyleAugmentor()
        # randomize style:
        im_restyled = augmentor(im_torch)
        Image.save(toPIL(im_restyled.squeeze().cpu()))

    except:
        print('{} is not converted')

