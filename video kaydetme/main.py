import cv2

# webcamdeki kareleri teker teker kaydedeceğimiz değişken burası
filename = "/Users/erimsaholut/PycharmProjects/Goruntu_isleme/video kaydetme/video.avi"
codec = cv2.VideoWriter_fourcc("W", "M", "V", "2")
frameRate = 30
resolution = (640, 480)
videoFileOutput = cv2.VideoWriter(filename, codec, frameRate, resolution)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    videoFileOutput.write(frame)
    cv2.imshow("Webcam", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
videoFileOutput.release()
cv2.destroyAllWindows()
