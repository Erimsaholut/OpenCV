import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255  # np.zero() belirli ölçülerle siyah ekran oluşturmak için
# print(canvas) dersek birsürü [0,0,0] yazıyor 000 siyah + 255 diyince hepsi beyaza dönüşüyor

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
