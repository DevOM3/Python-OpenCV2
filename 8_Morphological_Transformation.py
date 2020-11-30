import cv2
import numpy as np


cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_red = np.array([0, 0, 0])
    upper_red = np.array([255, 255, 255])

    mask = cv2.inRange(hsv, lower_red, upper_red)
    res = cv2.bitwise_and(frame, frame, mask=mask)

    kernel = np.ones((5, 5), np.uint8)
    erosion = cv2.erode(mask, kernel, iterations=1)     # erode one time ro the mask with he given kernel one time
    dilation = cv2.dilate(mask, kernel, iterations=1)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)    # This is to remove the False positive noise
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)   # This is to remove False negative noise

    cv2.imshow("Frame", frame)
    cv2.imshow("Res", res)
    cv2.imshow("Erosion", erosion)
    cv2.imshow("Dilation", dilation)
    cv2.imshow("Opening", opening)
    cv2.imshow("Closing", closing)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
