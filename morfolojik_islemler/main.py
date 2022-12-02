import cv2
import numpy as np

img = cv2.imread("Adsız 2.png")
kernel = np.ones((5, 5), np.uint8)
erosion = cv2.erode(img, kernel, iterations=5)
dilation = cv2.dilate(img, kernel, iterations=5)
gardient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

cv2.imshow("Title", img)
cv2.imshow("Kitle", erosion)
cv2.imshow("Fitne", dilation)
cv2.imshow("Fesat", gardient)
cv2.waitKey(0)
cv2.destroyAllWindows()
