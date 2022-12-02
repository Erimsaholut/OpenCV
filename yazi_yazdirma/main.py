import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

# cv2.yazıyaz(canvas,   "Ne yazcan"    ,başlaNok,  yazıtipi                kalınlık,renk,       yazı tipi ? )
cv2.putText(canvas, "OpenCV", (0, 256), cv2.FONT_HERSHEY_SIMPLEX, 5, (100, 0, 0), cv2.LINE_AA)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
