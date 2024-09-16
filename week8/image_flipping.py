from PIL import Image
img=Image.open('NPTEL/week8/mirror_ambulance.jpg')
#transposing
transposed_img=img.transpose(Image.FLIP_LEFT_RIGHT)
#save it to a file in a human understandable format
transposed_img.save('NPTEL/week8/corrected.jpg')
print('Done flipping')