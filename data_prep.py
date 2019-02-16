from PIL import Image, ImageFilter
import json

def data_prep(file,meta_file):
    im = Image.open(file)
    im = im.convert('L')
    w,h = im.size
    im = im.point(lambda x: 0 if x<128 else 255, '1')
    # im.save('result.jpg')
    for i in meta_file:
        a,b,x,y = meta_file[i]
        im.crop((a, b, w-x,h-y)).save( str(i) +".jpg")

# only for testing 
img = ("image.jpg")
meta = { "name" : (0, 100, 200,200), "roll" :  (100, 200, 600,500) }

if __name__ == "__main__":
    data_prep(img,meta)
