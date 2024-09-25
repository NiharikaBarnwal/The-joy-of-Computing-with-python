from PIL import Image
im=Image.open('testl.png')
rgb_im=im.convert('RGB')
r,g,b=rgb_im.getpixel( (150, 1) )
print(r,g,b)