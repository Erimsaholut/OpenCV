import cv2

# video dosyası açma
cap = cv2.VideoCapture("antalya.mp4")

# Web cam kullanma
# cap = cv2.VideoCapture("antalya.mp4")

# Video oynatma
while True:
    ret, frame = cap.read()
    if ret == 0:  # video biterse döngüyü kır
        break

    frame = cv2.flip(frame, 1)  # görüntüyü alıyor     # 1 framlelerin kaç saniye duracağını gösteriyor
    cv2.imshow("Amtalya", frame)  # görüntüyü gösteriyor
    if cv2.waitKey(10) & 0xFF == ord("q"):  # q tuşuna basılırsa döngüyü kır
        break

cap.release()
cv2.destroyAllWindows()
