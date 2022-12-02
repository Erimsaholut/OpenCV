import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("smile.jpg")
img2 = np.zeros((500, 500), np.uint8)
b, g, r = cv2.split(img)

cv2.rectangle(img2, (0, 0), (250, 250), (0, 0, 0), -1)

plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])

plt.show()

cv2.imshow("Title", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
