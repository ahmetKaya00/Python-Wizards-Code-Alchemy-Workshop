from math_operations import topla,cikar
import user_management as um

print("Modüler Programlama Örneği")

ad = input("Lütfen adınızı girin: ")
yas = int(input("Lütfen adınızı girin: "))

print(um.kullanici_kayit(ad,yas))

sifre = input("Şifrenizi oluşturun: ")
girilen_sifre = input("Giriş için şifrenizi girin: ")
print(um.kullanici_girisi(ad,sifre,girilen_sifre))

sayi1 = float(input("Birinci Sayıyı girin: "))
sayi2 = float(input("İkinci Sayıyı girin: "))

print("Toplam:", topla(sayi1,sayi2))
print("Çıkarma:", cikar(sayi1,sayi2))
