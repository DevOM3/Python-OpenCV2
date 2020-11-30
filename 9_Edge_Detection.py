import cv2

cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    laplacian = cv2.Laplacian(frame, cv2.CV_64F)    # laplation is used to show a antish image, mungya aaleli screen
    sobelx = cv2.Sobel(frame, cv2.CV_64F, 1, 0, ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame, 100, 200)

    cv2.imshow("Frame", frame)
    cv2.imshow("Laplacian", laplacian)
    cv2.imshow("Sobelx", sobelx)
    cv2.imshow("Sobely", sobely)
    cv2.imshow("EDGE", edges)

    if cv2.waitKey(5) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
