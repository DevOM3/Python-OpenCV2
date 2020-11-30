import cv2
import matplotlib.pyplot as plt

img1 = cv2.imread("opencv-feature-matching-image.jpg", 0)
img2 = cv2.imread("opencv-feature-matching-template.jpg", 0)

orb = cv2.ORB_create()

keyPoint1, descriptor1 = orb.detectAndCompute(img1, None)
keyPoint2, descriptor2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(descriptor1, descriptor2)
matches = sorted(matches, key=lambda x: x.distance)

img3 = cv2.drawMatches(img1, keyPoint1, img2, keyPoint2, matches[:21], None, flags=2)
plt.imshow(img3)
plt.show()
