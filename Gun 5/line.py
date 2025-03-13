import cv2
import numpy as np

image = np.zeros((500,500,3),dtype="uint8")

cv2.line(image,(50,50),(450,50),(0,255,0),3)
cv2.imshow("Çizgi Çizme",image)

cv2.rectangle(image,(100,100),(400,300),(255,0,0),3)
cv2.imshow("Dikdörtgen Çizme",image)

cv2.circle(image,(250,250),50,(0,0,255),2)
cv2.imshow("Çember Çizme",image)

points = np.array([[200,10],[300,250],[100,250]],np.int32)

cv2.polylines(image,[points],isClosed=True,color=(255,255,0),thickness=3)
cv2.imshow("Üçgen Çizme",image)

cv2.putText(image,"OPENCV ile Goruntu Olusturma",(50,450),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,255),2)
cv2.imshow("Yazı Çizme",image)
cv2.waitKey(0)
cv2.destroyAllWindows()