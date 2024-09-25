import scipy.misc
from PIL import Image
import numpy as np
import random
img=scipy.misc.imread('biahr.jpg')
count_bih=0
count_in=0
count=0
while(count<=10000):
    x=random.randint(0,898-1)
    y=random.randint(0,800-1)
    z=0
    if(img[x][y][z]==255):
        count_in=count_in+1
        count=count+1
    else:
        if(img[x][y][z]==251):
            count_bih=count_bih+1
            count=count+1
area_bih=(count_bih/count_in)*3287263
print(area_bih)