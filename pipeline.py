from PIL import Image, ImageOps, ImageDraw
import os
import random


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

    for i in range(1, 11):
      im = image.copy()
      draw = ImageDraw.Draw(im)
      draw.rectangle(((0,0),(400,200)), fill=(255, 255, 255))
      resized_image  = im.resize((50*i,50*i), Image.ANTIALIAS)


      draw.rectangle(((0,0),(200,400)), fill=(255, 255, 255))
      draw.rectangle(((0,200),(400,400)), fill=(255, 255, 255))
      draw.rectangle(((200,0),(400,400)), fill=(255, 255, 255))
      draw.rectangle(((200,200),(300,300)), fill=(255, 255, 255))
      draw.rectangle(((100,200),(200,300)), fill=(255, 255, 255))
      draw.rectangle(((100,200),(200,300)), fill=(255, 255, 255))
      draw.rectangle(((100,200),(300,300)), fill=(255, 255, 255))
      draw.rectangle(((100,200),(300,350)), fill=(255, 255, 255))
      draw.rectangle(((100,250),(300,300)), fill=(255, 255, 255))
      resized_image  = image.resize((100,100), Image.ANTIALIAS)




