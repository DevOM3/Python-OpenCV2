import cv2

cap = cv2.VideoCapture(0)   # capturing videos through webcam
fourcc = cv2.VideoWriter_fourcc(*'XVID')    # using the codex
out = cv2.VideoWriter('video.avi', fourcc, 20.0, (1920, 1080))  # specifying the outfile as- outfile, codec,_, file-size

while True:
    ret, frame = cap.read()  # here you will get bool in ret and frame in frame
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow("Color Frame", frame)
    cv2.imshow("Grey Frame", grey)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()   # releasing the camera
out.release()   # releasing the outfile to save the video
cv2.destroyAllWindows()  # destroying all windows
