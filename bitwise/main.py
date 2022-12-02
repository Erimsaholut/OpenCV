import cv2
import numpy as np

img1 = cv2.imread("bitwise_1.png")
img2 = cv2.imread("bitwise_2.png")
img3 = cv2.imread("/Users/erimsaholut/PycharmProjects/Goruntu_isleme/smoothing_images/filter.png")

xor = cv2.bitwise_xor(img1, img2)
kor = cv2.bitwise_or(img1, img2)
andı = cv2.bitwise_and(img1, img2)
nod = cv2.bitwise_not(img1)
nod2 = cv2.bitwise_not(img2)
not3 = cv2.bitwise_not(img3)

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("xor", xor)
cv2.imshow("kor", kor)
cv2.imshow("andı", andı)
cv2.imshow("not1", nod)
cv2.imshow("not2", nod2)
cv2.imshow("not3", not3)
cv2.waitKey(0)
cv2.destroyAllWindows()
