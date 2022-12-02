import cv2

img = cv2.imread("klon.jpg")

cv2.namedWindow("Title", cv2.WINDOW_NORMAL)
cv2.imshow("Title", img)
print(img.shape[:2])
# cv2.imwrite("deneme.jpg",img)
cv2.waitKey(0)

cv2.destroyAllWindows()
