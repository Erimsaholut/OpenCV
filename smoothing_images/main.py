import cv2

img1 = cv2.imread("filter.png")
img2 = cv2.imread("median.png")
img3 = cv2.imread("bilateral.png")

blur = cv2.blur(img1, (11, 11))
blur2 = cv2.GaussianBlur(img1, (11, 11), cv2.BORDER_DEFAULT)

median_blur = cv2.medianBlur(img2, 23)

bilateral_blur = cv2.bilateralFilter(img3, 9, 75, 75)
bilateral_blur2 = cv2.bilateralFilter(img3, 31, 100, 100)

cv2.imshow("blur", bilateral_blur2)
cv2.imshow("blur2", bilateral_blur)
cv2.imshow("original", img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
