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

new_width = 400
new_height = int(image.shape[0] * (new_width / image.shape[1]))
resized_image = cv2.resize(image,(new_width,new_height))

cv2.imshow("Boyutlandırılmış Görüntü",resized_image)
cv2.imwrite("resized_logo.png",resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

rotate_image = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Döndürülmüş Görüntü",rotate_image)
cv2.imwrite("rotate_image.png",rotate_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

cropped_image = image[50:250,50:250]
cv2.imshow("Kırpılmış Görüntü",cropped_image)
cv2.imwrite("cropped_image.png",cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()