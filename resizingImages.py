from PIL import Image, ImageOps
import os

bdir = "building_images"
ddir = 'dataset'
images = os.listdir(bdir)

SIZE = (400, 400)

for im in images:
  oim = Image.open(bdir+"/"+ im)
  padded_oim = ImageOps.pad(oim, SIZE, color="white")
  padded_oim.save(ddir+"/"+im)
