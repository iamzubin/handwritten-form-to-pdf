from PIL import Image, ImageFilter
import json, os

def data_prep(file,meta_file,PRE='tmp/'):
    im = Image.open(file)
    im = im.convert('L')
    w,h = im.size
    im = im.point(lambda x: 0 if x<128 else 255, '1')
    file_names = []
    for i in meta_file:
        a,b,x,y = meta_file[i]
        name = PRE + str(i) + '.png'
        im.crop((a, b, x, y)).save(name)
        file_names.append(name)
    return file_names


if __name__ == "__main__":
    # only for testing 
    img = ("test.png")
    meta = { 
            "name" : (100, 400, 2380, 550),
            "roll" :  (100, 550, 2380, 700),
            "address" : (100, 700, 2380, 1300)
    }
    data_prep(img,meta)