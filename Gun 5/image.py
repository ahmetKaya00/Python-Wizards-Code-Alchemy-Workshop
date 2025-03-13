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

h,w,c = image.shape

print(f"Görüntü Boyutları: {w}x{h} piksel, {c} kanal (RGB)")

image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("gray_logo.png", image_grey)
print("Gri tonlamalı görüntü kaydedildi: grey_logo.png")
cv2.imshow("Gri Görüntü",image_grey)
cv2.waitKey(0)
cv2.destroyAllWindows()