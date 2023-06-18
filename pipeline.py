from PIL import Image, ImageOps
import os

def resizingImages():
  bdir = "building_images"
  ddir = 'dataset'
  images = os.listdir(bdir)

  SIZE = (400, 400)

  for im in images:
    oim = Image.open(bdir+"/"+ im)
    padded_oim = ImageOps.pad(oim, SIZE, color="white")
    padded_oim.save(ddir+"/"+im)

def creatingClasses():
  ddir = "dataset"
  images = os.listdir(ddir)

  for i in range(len(images)):
    imname = images[i].split(".")[0]
    class_name = " ".join(imname.split("-"))
    print(f"  {i}: \'{class_name}\'")

def addDiversity():
  olddir = "dataset"
  newdir = "data"
  images = os.listdir(olddir)

  for iname in images:

    image = Image.open(olddir+"/"+iname)
    