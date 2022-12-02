import cv2
import numpy as np

img = cv2.imread("/Users/erimsaholut/PycharmProjects/Goruntu_isleme/smoothing_images/filter.png", 3)
img1 = cv2.imread("Mai_Sakurajima_Anime_-_Screenshot_1.png", 0)
img2 = cv2.imread("ll.png", 0)

row, col = img.shape[:2]

# resmi kaydırma
# M = np.float32([[1, 0, 0], [0, 1, 10]])
# dst = cv2.warpAffine(img, M, (row, col))
# cv2.imshow("dst", dst)

# yan çevirme
# M = cv2.getRotationMatrix2D((col / 2, row / 2), 90, 0.5)
# dst = cv2.warpAffine(img, M, (col, row))

# BU KISIM HEP resmin kenarlarini secmek için
#     ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY)
#     ret, th2 = cv2.threshold(img1, 110, 255, cv2.THRESH_BINARY)
#     ret, th3 = cv2.threshold(img2, 150, 255, cv2.THRESH_BINARY)
#
#     # cv2.imshow("İMG", img)
#     # cv2.imshow("IMMG", img1)
#     cv2.imshow("İMMG", img2)
#
#     # cv2.imshow("treshold", th1)
#     # cv2.imshow("treshold", th2)
#     cv2.imshow("treshold", th3)

ath = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow("ORİJİNAL", img1)
cv2.imshow("treshold", ath)

cv2.waitKey(0)
cv2.destroyAllWindows()
