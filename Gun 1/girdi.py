isim = input("Adınızı girin: ")
print(f"Merhaba, {isim}")

yas = int(input("Yaşınızı girin: "))
print(f"Gelecek yıl, {yas + 1} yaşında olacaksınız")

isim, yas = input("Adınızı ve yaşınızı girin (Boşluk ile ayırın): ").split()
yas = int(yas)

print("Adınız: ", isim)
print("Yaşınız: ", yas)

try:
    yas = int(input("Yaşınızı Girin: "))
    print("Yaşınız ",yas)
except ValueError:
    print("Hatalı giriş! Lütfen Tam Sayı Girin!")

import getpass

sifre = getpass.getpass("Şifrenizi girin: ")
print("Şifreniz başarılı bir şekilde kayıt edildi")