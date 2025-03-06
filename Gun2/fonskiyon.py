print("Merhaba, Ahmet")
print("Merhaba, Mehmet")
print("Merhaba, Ayşe")

def selamla(isim):
    print(f"Merhaba, {isim}")

selamla("Ahmet")

def topla(a,b):
    toplam = a + b
    return toplam

print("Sunuç: ", topla(3,5))

def merhaba(isim="Misafir"):
    print(f"Merhaba, {isim}")

merhaba()

def islemler(sayi):
    kare = sayi ** 2
    kup = sayi ** 3
    return kare, kup

sonuc1, sonuc2 = islemler(3)
print("Karesi: ",sonuc1)
print("Küpü: ",sonuc2)

def kup_al(x):
    return x ** 3

print(kup_al(3))

kup_al = lambda x: x**3

print(kup_al(5))

def cift_mi(sayi):
    return sayi % 2 == 0

def sayiyi_kontrol_et(sayi):
    if cift_mi(sayi):
        print(f"{sayi} çifttir.")
    else:
        print(f"{sayi} tektir.")

sayiyi_kontrol_et(10)
sayiyi_kontrol_et(7)

def topla(a,b):
    return a+b
def cikar(a,b):
    return a-b
def carp(a,b):
    return a*b
def bol(a,b):
    if b == 0:
        return "Hata: Sıfıra bölme hatası!"
    return a / b

sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

print("İşlem Seçin: +,-,*,/")
islem = input("İşlem: ")

if islem == "+":
    print("Sonuç:", topla(sayi1,sayi2))
elif islem == "-":
    print("Sonuç:", cikar(sayi1,sayi2))
elif islem == "*":
    print("Sonuç:", carp(sayi1,sayi2))
elif islem == "/":
    print("Sonuç:", bol(sayi1,sayi2))
else:
    print("Geçersiz işlem!")