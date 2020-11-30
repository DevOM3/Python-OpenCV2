import cv2

cap = cv2.VideoCapture('people-walking.mp4')
fgbg = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)  # applying MOG2 background subtractor

    cv2.imshow("Original", frame)
    cv2.imshow("Masked", fgmask)

    if cv2.waitKey(30) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
