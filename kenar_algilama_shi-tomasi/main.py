import numpy as np
import cv2

text = cv2.imread("text.png")
contour = cv2.imread("contour.png")

gray_version = cv2.cvtColor(text, cv2.COLOR_BGR2GRAY)
gray_version = np.float32(gray_version)

corners = cv2.goodFeaturesToTrack(gray_version, 75, 0.01, 10)

corners = np.int0(corners)
for corner in corners:
    x, y = corner.ravel()
    cv2.circle(text, (x, y), 3, (255, 0, 0), -1)

cv2.imshow("corner", text)
cv2.waitKey(0)
cv2.destroyAllWindows()
