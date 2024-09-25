from PIL import Image
import random
im=Image.open('NPTEL/week9/bihar.jpg')
rgb_im=im.convert('RGB')
width, height = im.size
count_bih=0
count_in=0
count=0
while(count<=100000):
    x=random.randint(0,width-1)
    y=random.randint(0,height-1)
    z=0
    r,g,b=rgb_im.getpixel((x,y))
    if(r==255):
        count_in=count_in+1
        count=count+1
    else:
        if(r in (251,253)):
            count_bih=count_bih+1
            count=count+1
area_bih=(count_bih/count_in)*3287263
print(area_bih)