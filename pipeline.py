from PIL import Image, ImageOps, ImageDraw
import os
import random
import numpy as np

SIZE = (400, 400)

NAMES_FLIPPED = {

  'canon geared up 19' : 0,
  'dark barracks 4' : 1,
  'canon 20' : 2,
  'army camp 10' : 3,
  'dark spell factory 2' : 4,
  'canon 21' : 5,
  'canon 3' : 6,
  'gold mine 4' : 7,
  'army camp 1' : 8,
  'elixir storage 15' : 9,
  'town hall 12 5' : 10,
  'inferno tower 1' : 11,
  'town hall 14 2' : 12,
  'canon geared up 17' : 13,
  'archer tower fast attack 10' : 14,
  'laboratory 5' : 15,
  'x bow 5' : 16,
  'archer tower fast attack 18' : 17,
  'canon geared up 21' : 18,
  'laboratory 7' : 19,
  'x bow 4' : 20,
  'air sweeper 1' : 21,
  'clan castle 3' : 22,
  'pet house 6' : 23,
  'town hall 15 4' : 24,
  'army camp 2' : 25,
  'air defense 11' : 26,
  'town hall 10' : 27,
  'clan castle 2' : 28,
  'laboratory 13' : 29,
  'archer tower 4' : 30,
  'elixir collector 9' : 31,
  'hidden tesla 13' : 32,
  'wall 7' : 33,
  'barracks 8' : 34,
  'spell factory 7' : 35,
  'gold storage 7' : 36,
  'scattershot 3' : 37,
  'archer tower 15' : 38,
  'dark elixir storage 9' : 39,
  'army camp 9' : 40,
  'mortar burst fire 8' : 41,
  'hidden tesla 6' : 42,
  'bomb tower 7' : 43,
  'canon 8' : 44,
  'gold storage 4' : 45,
  'canon 14' : 46,
  'air sweeper 2' : 47,
  'spell factory 4' : 48,
  'tornado trap 2,3' : 49,
  'spell factory 2' : 50,
  'canon geared up 16' : 51,
  'bomb tower 4' : 52,
  'gold mine 7' : 53,
  'mortar 14' : 54,
  'archer tower long range 15' : 55,
  'wizard tower 13' : 56,
  'elixir collector 11' : 57,
  'canon 6' : 58,
  'archer tower 17' : 59,
  'canon 1' : 60,
  'laboratory 2' : 61,
  'elixir collector 8' : 62,
  'scattershot 1' : 63,
  'mortar 7' : 64,
  'elixir collector 14' : 65,
  'gold storage 13' : 66,
  'town hall 6' : 67,
  'mortar 11' : 68,
  'hidden tesla 9' : 69,
  'archer tower fast attack 14' : 70,
  'mortar 3' : 71,
  'mortar burst fire 12' : 72,
  'hidden tesla 11' : 73,
  'gold storage 10' : 74,
  'archer tower 20' : 75,
  'wall 2' : 76,
  'elixir storage 12' : 77,
  'spell factory 6' : 78,
  'workshop 1' : 79,
  'bomb tower 3' : 80,
  'giant bomb 7,8' : 81,
  'dark elixir storage 3' : 82,
  'dark elixir drill 5' : 83,
  'workshop 4' : 84,
  'town hall 9' : 85,
  'town hall 13 1' : 86,
  'canon geared up 9' : 87,
  'giant bomb 3,4' : 88,
  'bobs hut' : 89,
  'gold storage 8' : 90,
  'elixir collector 4' : 91,
  'dark elixir storage 2' : 92,
  'army camp 12' : 93,
  'eagle artillery 6' : 94,
  'mortar burst fire 10' : 95,
  'wall 12' : 96,
  'air bomb 1,2' : 97,
  'army camp 7' : 98,
  'wizard tower 7' : 99,
  'gold storage 9' : 100,
  'dark elixir storage 7' : 101,
  'gold storage 14' : 102,
  'mortar geared up 13' : 103,
  'archer tower 3' : 104,
  'mortar geared up 8' : 105,
  'skeleton trap 3,4' : 106,
  'archer tower 7' : 107,
  'laboratory 4' : 108,
  'town hall 12 4' : 109,
  'archer tower long range 14' : 110,
  'dark elixir drill 8' : 111,
  'dark elixir drill 9' : 112,
  'wizard tower 12' : 113,
  'poison spell tower 2' : 114,
  'canon geared up burst 20' : 115,
  'wizard tower 1' : 116,
  'mortar burst fire 15' : 117,
  'barracks 11' : 118,
  'bomb tower 1' : 119,
  'laboratory 10' : 120,
  'hidden tesla 1' : 121,
  'canon geared up burst 12' : 122,
  'dark elixir drill 1' : 123,
  'bomb 5,6' : 124,
  'mortar 9' : 125,
  'elixir storage 7' : 126,
  'mortar 13' : 127,
  'barracks 2' : 128,
  'elixir collector 2' : 129,
  'laboratory 1' : 130,
  'spring trap 5' : 131,
  'invisibility spell tower 3' : 132,
  'gold mine 9' : 133,
  'seeking air mine 1,2' : 134,
  'hidden tesla 7' : 135,
  'elixir collector 10' : 136,
  'archer tower long range 19' : 137,
  'mortar 15' : 138,
  'giant bomb 9' : 139,
  'eagle artillery 2' : 140,
  'x bow 9' : 141,
  'builders hut weaponized 4' : 142,
  'canon 18' : 143,
  'archer tower fast attack 17' : 144,
  'air bomb 7,8' : 145,
  'army camp 5' : 146,
  'archer tower 19' : 147,
  'dark barracks 6' : 148,
  'pet house 7' : 149,
  'monolith 2' : 150,
  'archer tower fast attack 11' : 151,
  'rage spell tower 1' : 152,
  'spell factory 5' : 153,
  'workshop 2' : 154,
  'eagle artillery 4' : 155,
  'town hall 15 2' : 156,
  'archer tower 5' : 157,
  'archer tower fast attack 12' : 158,
  'laboratory 6' : 159,
  'wizard tower 5' : 160,
  'bomb tower 5' : 161,
  'elixir storage 6' : 162,
  'archer tower 9' : 163,
  'gold mine 12' : 164,
  'archer tower 1' : 165,
  'town hall 13 3' : 166,
  'canon geared up 10' : 167,
  'gold mine 14' : 168,
  'canon geared up burst 10' : 169,
  'tornado trap 1' : 170,
  'builders hut 5' : 171,
  'elixir storage 16' : 172,
  'air defense 13' : 173,
  'archer tower long range 18' : 174,
  'army camp 4' : 175,
  'wall 11' : 176,
  'wizard tower 6' : 177,
  'barracks 14' : 178,
  'mortar 4' : 179,
  'town hall 14 1' : 180,
  'canon geared up 12' : 181,
  'elixir storage 11' : 182,
  'builders hut weaponized 3' : 183,
  'dark elixir drill 2' : 184,
  'gold mine 11' : 185,
  'builders hut 3' : 186,
  'laboratory 8' : 187,
  'town hall 5' : 188,
  'archer tower long range 10' : 189,
  'bomb tower 2' : 190,
  'wall 6' : 191,
  'air defense 2' : 192,
  'archer tower 6' : 193,
  'barracks 13' : 194,
  'town hall 11' : 195,
  'town hall 13 4' : 196,
  'wizard tower 4' : 197,
  'hidden tesla 10' : 198,
  'gold storage 12' : 199,
  'canon 17' : 200,
  'wall 15png' : 201,
  'spell factory 3' : 202,
  'canon geared up 14' : 203,
  'bomb tower 8' : 204,
  'archer tower 21' : 205,
  'air defense 9' : 206,
  'archer tower 11' : 207,
  'archer tower long range 11' : 208,
  'elixir collector 7' : 209,
  'scattershot 4' : 210,
  'town hall 15 3' : 211,
  'bomb 1,2' : 212,
  'wall 10' : 213,
  'hidden tesla 12' : 214,
  'town hall 14 5' : 215,
  'air defense 4' : 216,
  'gold mine 5' : 217,
  'canon geared up burst 9' : 218,
  'canon geared up burst 13' : 219,
  'builders hut 1' : 220,
  'elixir collector 1' : 221,
  'elixir storage 1' : 222,
  'barracks 10' : 223,
  'gold mine 10' : 224,
  'pet house 8' : 225,
  'gold storage 16' : 226,
  'laboratory 11' : 227,
  'x bow 1' : 228,
  'mortar burst fire 11' : 229,
  'dark barracks 3' : 230,
  'archer tower long range 20' : 231,
  'x bow 6' : 232,
  'dark elixir storage 4' : 233,
  'mortar burst fire 14' : 234,
  'air defense 10' : 235,
  'mortar 6' : 236,
  'elixir collector 15' : 237,
  'dark barracks 8' : 238,
  'town hall 15 5' : 239,
  'canon 7' : 240,
  'wall 16' : 241,
  'clan castle 6' : 242,
  'elixir collector 3' : 243,
  'mortar geared up 10' : 244,
  'x bow 3' : 245,
  'rage spell tower 2' : 246,
  'mortar 2' : 247,
  'archer tower fast attack 21' : 248,
  'workshop 3' : 249,
  'air bomb 9' : 250,
  'workshop 7' : 251,
  'pet house 1' : 252,
  'canon geared up burst 19' : 253,
  'town hall 12 1' : 254,
  'gold mine 2' : 255,
  'barracks 15' : 256,
  'workshop 5' : 257,
  'army camp 3' : 258,
  'mortar geared up 14' : 259,
  'wall 8' : 260,
  'wizard tower 15' : 261,
  'dark spell factory 4' : 262,
  'inferno tower 5' : 263,
  'wall 4' : 264,
  'canon 15' : 265,
  'town hall 4' : 266,
  'wizard tower 3' : 267,
  'barracks 6' : 268,
  'dark elixir storage 10' : 269,
  'barracks 7' : 270,
  'gold mine 1' : 271,
  'archer tower 14' : 272,
  'wall 14' : 273,
  'elixir storage 2' : 274,
  'town hall 12 3' : 275,
  'spell factory 1' : 276,
  'archer tower long range 13' : 277,
  'air defense 7' : 278,
  'wall 13' : 279,
  'grand warden altar' : 280,
  'town hall 7' : 281,
  'monolith 1' : 282,
  'canon geared up burst 14' : 283,
  'archer tower fast attack 19' : 284,
  'mortar 12' : 285,
  'elixir storage 5' : 286,
  'wizard tower 2' : 287,
  'canon geared up burst 11' : 288,
  'x bow 8' : 289,
  'archer tower long range 17' : 290,
  'canon geared up 11' : 291,
  'canon geared up burst 15' : 292,
  'dark elixir drill 6' : 293,
  'dark barracks 2' : 294,
  'elixir storage 8' : 295,
  'inferno tower 2' : 296,
  'army camp 6' : 297,
  'archer tower 10' : 298,
  'clan castle 1' : 299,
  'dark barracks 9' : 300,
  'canon 12' : 301,
  'canon geared up 15' : 302,
  'gold storage 5' : 303,
  'x bow 10' : 304,
  'barracks 16' : 305,
  'dark barracks 7' : 306,
  'dark spell factory 3' : 307,
  'barracks 3' : 308,
  'dark elixir storage 1' : 309,
  'elixir storage 13' : 310,
  'pet house 4' : 311,
  'barracks 12' : 312,
  'builders hut 4' : 313,
  'gold storage 3' : 314,
  'town hall 8' : 315,
  'canon 5' : 316,
  'hidden tesla 2' : 317,
  'barbarian king altar' : 318,
  'mortar 8' : 319,
  'archer tower long range 12' : 320,
  'builders hut weaponized 2' : 321,
  'hidden tesla 5' : 322,
  'skeleton trap 1,2' : 323,
  'archer tower fast attack 20' : 324,
  'elixir collector 6' : 325,
  'eagle artillery 5' : 326,
  'elixir storage 3' : 327,
  'canon 2' : 328,
  'pet house 2' : 329,
  'air defense 12' : 330,
  'air defense 8' : 331,
  'barracks 1' : 332,
  'mortar geared up 12' : 333,
  'wizard tower 9' : 334,
  'canon 9' : 335,
  'eagle artillery 1' : 336,
  'dark elixir drill 7' : 337,
  'canon geared up 7' : 338,
  'mortar geared up 9' : 339,
  'elixir storage 4' : 340,
  'elixir storage 9' : 341,
  'hidden tesla 8' : 342,
  'wall 9' : 343,
  'army camp 8' : 344,
  'inferno tower 7' : 345,
  'elixir collector 12' : 346,
  'archer tower 12' : 347,
  'workshop 6' : 348,
  'gold storage 2' : 349,
  'wizard tower 8' : 350,
  'canon geared up 18' : 351,
  'archer tower long range 16' : 352,
  'mortar geared up 15' : 353,
  'spring trap 1,2' : 354,
  'bomb tower 10' : 355,
  'inferno tower 3' : 356,
  'wall 3' : 357,
  'air defense 6' : 358,
  'bomb 9,10' : 359,
  'air bomb 3,4' : 360,
  'archer tower fast attack 15' : 361,
  'air bomb 5,6' : 362,
  'pet house 3' : 363,
  'dark barracks 1' : 364,
  'archer tower fast attack 16' : 365,
  'x bow 2' : 366,
  'archer tower 18' : 367,
  'royal champion altar' : 368,
  'canon 10' : 369,
  'mortar 10' : 370,
  'air defense 5' : 371,
  'gold storage 15' : 372,
  'spring trap 3,4' : 373,
  'air sweeper 5' : 374,
  'giant bomb 1,2' : 375,
  'hidden tesla 14' : 376,
  'bomb 11' : 377,
  'elixir storage 10' : 378,
  'canon geared up 20' : 379,
  'gold mine 15' : 380,
  'mortar 5' : 381,
  'air sweeper 6' : 382,
  'dark elixir storage 8' : 383,
  'dark elixir storage 6' : 384,
  'town hall 13 2' : 385,
  'canon geared up burst 16' : 386,
  'seeking air mine 5' : 387,
  'canon geared up burst 17' : 388,
  'inferno tower 9' : 389,
  'archer tower long range 21' : 390,
  'clan castle 8' : 391,
  'archer tower 16' : 392,
  'mortar 1' : 393,
  'pet house 5' : 394,
  'elixir collector 13' : 395,
  'laboratory 3' : 396,
  'gold storage 11' : 397,
  'town hall 15 1' : 398,
  'archer tower 13' : 399,
  'canon 16' : 400,
  'scattershot 2' : 401,
  'bomb tower 9' : 402,
  'wall 5' : 403,
  'wall 1' : 404,
  'clan castle 10' : 405,
  'canon geared up burst 21' : 406,
  'dark spell factory 5' : 407,
  'bomb 7,8' : 408,
  'canon 4' : 409,
  'clan castle 5' : 410,
  'canon geared up burst 18' : 411,
  'inferno tower 4' : 412,
  'archer queen altar' : 413,
  'mortar geared up 11' : 414,
  'rage spell tower 3' : 415,
  'gold mine 3' : 416,
  'elixir storage 14' : 417,
  'eagle artillery 3' : 418,
  'barracks 5' : 419,
  'clan castle 4' : 420,
  'air sweeper 3' : 421,
  'canon 13' : 422,
  'poison spell tower4' : 423,
  'town hall 3' : 424,
  'wizard tower 10' : 425,
  'gold storage 6' : 426,
  'wizard tower 14' : 427,
  'hidden tesla 4' : 428,
  'bomb 3,4' : 429,
  'elixir collector 5' : 430,
  'hidden tesla 3' : 431,
  'wizard tower 11' : 432,
  'inferno tower 6' : 433,
  'archer tower 2' : 434,
  'canon 11' : 435,
  'town hall 14 4' : 436,
  'town hall 2' : 437,
  'canon geared up 8' : 438,
  'archer tower fast attack 13' : 439,
  'dark barracks 10' : 440,
  'air sweeper 4' : 441,
  'dark elixir drill 3' : 442,
  'giant bomb 5,6' : 443,
  'clan castle 11' : 444,
  'laboratory 12' : 445,
  'clan castle 9' : 446,
  'mortar burst fire 9' : 447,
  'barracks 9' : 448,
  'air defense 1' : 449,
  'builders hut weaponized 5' : 450,
  'mortar burst fire 13' : 451,
  'x bow 7' : 452,
  'dark spell factory 1' : 453,
  'barracks 4' : 454,
  'town hall 12 2' : 455,
  'army camp 11' : 456,
  'canon geared up 13' : 457,
  'dark barracks 5' : 458,
  'builders hut 2' : 459,
  'bomb tower 6' : 460,
  'air sweeper 7' : 461,
  'town hall 14 3' : 462,
  'clan castle 7' : 463,
  'town hall 1' : 464,
  'air defense 3' : 465,
  'archer tower 8' : 466,
  'gold mine 8' : 467,
  'dark elixir storage 5' : 468,
  'gold storage 1' : 469,
  'gold mine 6' : 470,
  'dark elixir drill 1' : 471,
  'canon 19' : 472,
  'laboratory 9' : 473,
  'inferno tower 8' : 474,
  'town hall 13 5' : 475,
  'canon geared up burst 7' : 476,
  'seeking air mine 3,4' : 477,
  'gold mine 13' : 478,
  'canon geared up burst 8' : 479,

}


def resizingImages():
  bdir = "building_images"
  ddir = 'dataset'
  images = os.listdir(bdir)

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

"""
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

"""

def addDiversity():

  olddir = "dataset"
  images = os.listdir(olddir)

  for image_name in images:
    image = Image.open(olddir + "/" + image_name)

    #make 100 versions of image
    for i in range(100):

      im = image.copy()
      draw = ImageDraw.Draw(im)

      #DRAW RECTANGLES
      #i: 0-24 = left, 25-49 = right, 50-74 = bottom, 75-99 = middle
      if i < 25:

        tl = (0, random.randint(0, 150))
        br = (200, random.randint(250, 400))
        draw.rectangle((tl,br), fill=(255, 255, 255))

      elif i < 50:

        tl = (200, random.randint(0, 150))
        br = (400, random.randint(250, 400))
        draw.rectangle((tl,br), fill=(255, 255, 255))
        
      elif i < 75:

        tl = (random.randint(0, 150), 200)
        br = (random.randint(250, 400), 400)
        draw.rectangle((tl,br), fill=(255, 255, 255))
        
      else:
        
        tl = (random.randint(100, 150), random.randint(100, 150))
        br = (random.randint(250, 300), random.randint(250, 300))
        draw.rectangle((tl,br), fill=(255, 255, 255))


      #RESIZE AND REPAD
      #50, 100, 150, 200, 250, 300, 350, 400

      match i%8:
        case 0:
          resized_image  = im.resize((50,50), Image.ANTIALIAS)
        case 1:
          resized_image  = im.resize((100,100), Image.ANTIALIAS)
        case 2:
          resized_image  = im.resize((150,150), Image.ANTIALIAS)
        case 3:
          resized_image  = im.resize((200,200), Image.ANTIALIAS)
        case 4:
          resized_image  = im.resize((250,250), Image.ANTIALIAS)
        case 5:
          resized_image  = im.resize((300,300), Image.ANTIALIAS)
        case 6:
          resized_image  = im.resize((350,350), Image.ANTIALIAS)
        case 7:
          resized_image  = im.resize((400,400), Image.ANTIALIAS)

      #padding image
      padded_image = Image.new("RGB", (400, 400), (255, 255, 255))
      padded_image.paste(resized_image, ((400-resized_image.size[0])//2, (400-resized_image.size[1])//2))

      #save images to correct folders
      image_name = image_name.split(".")[0]
      name = str(image_name+str(i))
      if i%10 == 0:
        padded_image.save("data/valid/images/"+name+".png")
      else:
        padded_image.save("data/train/images/"+name+".png")

      #LABELS

      #getting class number
      image_n = images[i].split(".")[0]
      class_name = " ".join(image_n.split("-"))

      class_num = NAMES_FLIPPED[class_name]

      #getting center, width, and height
      arr = np.array(padded_image)

      #find left-most and right-most non-white pixels
      leftedge = -1
      rightedge = -1
      for x in range(400):
        s = sum(sum(arr[:,x] - 255))
        if s > 0 and leftedge == -1:
          leftedge = x
        if s > 0:
          rightedge = x

      #find top-most and bottom-most non-white pixels
      topedge = -1
      bottomedge = -1
      for y in range(400):
        s = sum(sum(arr[y,:] - 255))
        if s > 0 and topedge == -1:
          topedge = y
        if s > 0:
          bottomedge = y

      centerx = (leftedge + rightedge) / 800
      centery = (topedge + bottomedge) / 800

      w = (rightedge - leftedge) / 400
      h = (bottomedge - topedge) / 400


      if i%10 == 0:
        f = open("data/valid/labels/"+name+".txt", "w")

      else:
        f = open("data/train/labels/"+name+".txt", "w")

      f.write(str(class_num) + " " + str(centerx) + " " + str(centery) + " " + str(w) + " " + str(h))
      f.close()

      
addDiversity()