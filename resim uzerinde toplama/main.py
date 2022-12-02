import cv2
import numpy as np

circle = np.zeros((512, 512, 3), dtype=np.uint8) + 255
rectangle = np.zeros((512, 512, 3), dtype=np.uint8) + 255

cv2.circle(circle, (256, 256), 150, (0, 0, 255), thickness=-1)
cv2.rectangle(rectangle, (156, 156), (356, 356), (0, 255, 0), thickness=-1)

son = cv2.add(circle, rectangle)

dst = cv2.addWeighted(circle, 1, rectangle, 1, 0)

cv2.imshow("Daire", circle)
cv2.imshow("Kare", rectangle)
cv2.imshow("Son", son)
cv2.imshow("Karışık", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()