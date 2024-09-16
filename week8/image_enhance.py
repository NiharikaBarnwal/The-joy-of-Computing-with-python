import cv2
img = cv2.imread("NPTEL/week8/Blurry-picture.jpg")
# Preparation of CLAHE
clahe=cv2.createCLAHE()
# Convert to gray scale image
gray_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Apply enhancement
enh_img = clahe.apply(gray_image)
#save it to a file
cv2.imwrite('NPTEL/week8/enhanced.jpg', enh_img)
print('Done enhancing')