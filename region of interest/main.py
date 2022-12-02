import cv2

img = cv2.imread("klon.jpg")

print(img.shape[:2])
# (426, 640)

cv2.imshow("klon", img)

roi = img[180:420, 430:640]

cv2.imshow("ROI", roi)

cv2.waitKey()
cv2.destroyAllWindows()
