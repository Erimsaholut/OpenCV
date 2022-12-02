import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

# çizgi(canvasseç,başlangıç,bitiş nok,boyanın rengi,boya kalınlığı)
cv2.line(canvas, (00, 00), (512, 512), (0, 255, 0), thickness=5)
cv2.line(canvas, (512, 00), (0, 512), (0, 255, 0), thickness=5)

# cv2.dik4gen(cenvasseç,sağüst,solalt          renk          kalınlık)
cv2.rectangle(canvas, (50, 50), (450, 450), (255, 0, 0), thickness=5)
#                                                          kalınlık -1 olursa içini dolduruyor
cv2.rectangle(canvas, (226, 226), (286, 286), (0, 0, 255), thickness=-1)
# cv2.daire(canvasseç,merkezseç,yarıçap ,renkseç,      kalınlık) doldurak için -1
cv2.circle(canvas, (256, 256), 150, (100, 100, 100), thickness=10)

# üçgen fonksiyonu yok 3 tane çizgi falan çiziliyor
cv2.line(canvas, (200, 200), (312, 200), (0, 0, 0), thickness=5)
cv2.line(canvas, (200, 200), (256, 256), (0, 0, 0), thickness=5)
cv2.line(canvas, (256, 256), (312, 200), (0, 0, 0), thickness=5)

# noktalar dizioluştur([[n1],[n2],[n3],... , ..., [n31]],np.int32)
points = np.array([[100, 225], [300, 150], [450, 133], [323, 213], [31, 31]], np.int32)
# cv2.bisürüçizgi(canvasseç,noktalar,kapalıOlsunMu,Renk,Kalınlık)
cv2.polylines(canvas, [points], True, (200, 200, 200), thickness=5)

# cv2.elips(canvasseç,merkeznok,genişlik&yükseklik,yatayla açısı,derecebaşla,derecebitir,renk,kalınlık)
cv2.ellipse(canvas, (200, 250), (80, 20), 10, 0, 360, (31, 31, 31), -1)



cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
