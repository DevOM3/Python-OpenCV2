import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    cv2.line(frame, (0, 0), (111, 111), (0, 0, 255), 11)    # drawing on frame, from point, to point, in color, of width
    cv2.rectangle(frame, (0, 0), (111, 111), (0, 0, 0), 4)  # parameters as as above
    cv2.circle(frame, (222, 222), 51, (255, 255, 255), -1)  # making a circle on frame, with center point of radius, of color, with width given in negative 1 which means to fill it

    pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int_)
    cv2.polylines(frame, [pts], True, (1, 255, 214))     # create a polygon on frame with points, join the last point to the first, color

    # writing on frame
    font = cv2.FONT_HERSHEY_PLAIN
    cv2.putText(frame, "My name is OM", (0, 130), font, 1, (0, 0, 0), 7)  # Write "My name is OM" on frame at point (0, 130) with given font, of size, of color, of thickness

    cv2.imshow("Drawing Frame", frame)

    if cv2.waitKey(0):
        break

cap.release()
cv2.destroyAllWindows()
