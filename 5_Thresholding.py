import cv2
import numpy as np

img = cv2.imread("bookpage.jpg")    # reading the image

ret, threashold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)    # thresholding the image and converting every pixel
# having value greater than 12 to the 255

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    # converting image to grayscale
ret2, threshold2 = cv2.threshold(gray, 12, 255, cv2.THRESH_BINARY)

# creating an adaptiveThreshold()
gaus = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
# above line has max-pixel-value 255 and it is adaptive

ret3, otsu = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow("Image", img)
cv2.imshow("Threashold", threashold)
cv2.imshow("Threashold2", threshold2)
cv2.imshow("Gaussian", gaus)
cv2.imshow("OTSU", otsu)


cv2.waitKey(0)
cv2.destroyAllWindows()
