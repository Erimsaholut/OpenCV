import cv2

img = cv2.imread("/Users/erimsaholut/PycharmProjects/Goruntu_isleme/pikseller/klon.jpg")
img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img2 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("BGR ORJ", img)
cv2.imshow("RGB REP", img1)
cv2.imshow("HSV REP", img2)
cv2.imshow("GRAY REP", img3)

cv2.waitKey(0)
cv2.destroyAllWindows()
