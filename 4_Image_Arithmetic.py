import cv2
import numpy as np

img1 = cv2.imread("OFFchatTemplae.png")
img2 = cv2.imread("icon1.png")

'''=================================================================================================================='''

# If we add two images with +
# img1 + img2
# it will add images

'''=================================================================================================================='''

# if we use cv2.add(img1, img2) to add them it will add pixel values

'''=================================================================================================================='''

#  addWeighted(img1, 0.6, img2, 0.4, 0)
#  above code is used to show img1 60% and img2 40% in as single image with gama 0

'''=================================================================================================================='''

rows, cols, channels = img2.shape   # this returns the 3D value
roi = img1[0:rows, 0:cols]  # getting the region of image img1 from top left corner to the size of the img2

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)   # converting the image to grayscale
ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)    # threasholding an image to convert every pixel
# having value greater than 220 to 255

mask_inv = cv2.bitwise_not(mask)    # inverting the black and white colors

img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow("Image", img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
