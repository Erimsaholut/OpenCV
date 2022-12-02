import cv2
import numpy as np

img = cv2.imread("klon.jpg")

color = img[150, 200]
print("BGR: ", color)
print("Blue: ", color[0])
print("Green: ", color[1])
print("Red: ", color[2])

img[150, 200] = [0, 0, 0]
color = img[150, 200]

print("Blue: ", color[0])

img.itemset((150, 200, 0), 31)
blue1 = img.item(150, 200, 0)
print(f"Mavi yeni: {blue1}")

cv2.imshow("Title", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
