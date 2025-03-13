import cv2
from PIL import Image
import numpy as np

image_path = "logo.png"

image = cv2.imread(image_path)

if image is None:
    print("Hata: Görüntü dosyası bulunamadı!")
    exit()

print("Görüntü başarıyla yüklendi.")

cv2.imshow("Orijinal Görüntü",image)

cv2.waitKey(0)
cv2.destroyAllWindows()

blue_channel, green_channel, red_channel = cv2.split(image)
cv2.imshow("Mavi Kanal", blue_channel)
cv2.imshow("Yeşil Kanal", green_channel)
cv2.imshow("Kırmızı Kanal", red_channel)
cv2.waitKey(0)
cv2.destroyAllWindows()

modified_image = cv2.merge([green_channel,red_channel,blue_channel])

cv2.imshow("Değiştirilmiş Renkler",modified_image)
cv2.imwrite("modified_image.png",modified_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

hsv_image = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_red = np.array([0,120,70])
upper_red= np.array([10,255,255])

mask = cv2.inRange(hsv_image,lower_red,upper_red)

cv2.imshow("Kırmızı Renk Maskesi",mask)
cv2.imwrite("red_mask.png",mask)
cv2.waitKey(0)
cv2.destroyAllWindows()
