import cv2

cap = cv2.VideoCapture("antalya.mp4")

while True:
    ret, frame = cap.read()

    if ret == 0:
        break
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # cv2.COLOR_BGR2HSV,cv2.COLOR_BGR2RGB,cv2.COLOR_BGR2GRAY
    frame = cv2.flip(frame, 1)


    cv2.imshow("Amtalya", frame)
    if cv2.waitKey(31) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
