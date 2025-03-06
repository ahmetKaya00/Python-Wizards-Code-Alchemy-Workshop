print("merhaba")

#print(10/0)

#print("Merhaba" + 5)
"""
liste = [1,2,3]
print(liste[5])
"""
try:
    x = int(input("Bir sayı giriniz: "))
    print(f"Girdiğiniz sayı: {x}")
except ValueError:
    print("Hata: Lütfen geçerli bir sayı giriniz!")

print("merhaba")

try:
    dosya = open("ornek.txt","r")
    icerik = dosya.read()
    print(icerik)
except FileNotFoundError:
    print("Dosya bulunamadı!")
finally:
    dosya.close()
    print("Dosya kapatıldı")

def bolme(a,b):
    if b == 0:
        raise ZeroDivisionError("Bir sayı sıfıra bölünemez!")
    return a / b

print(bolme(10,2))

class NegatifSayiSatasi(Exception):
    pass

def karekok_al(sayi):
    if sayi < 0:
        raise NegatifSayiSatasi("Negatif sayıların karekökü alınmaz!")
    return sayi ** 0.5

print(karekok_al(34))