import getpass

print("Kullanıcı Kayıt Ekranı")

ad = input("Adınızı girin: ")

while True:
    try:
        yas = int(input("Yaşınızı girin: "))
        if yas < 18:
            print("Üzgünüm, 18 yaşından küçükler sisteme kayıt olamaz")
            exit()
        break
    except ValueError:
        print("Hatalı giriş! Lütfen sadece sayı girin.")

while True:
    sifre = getpass.getpass("Şifrenizi oluşturun: ")
    sifre_tekrar = getpass.getpass("Şifrenizi tekrar girin: ")

    if sifre == sifre_tekrar:
        print("Şifre başarılı bir şekilde oluşturuldu.")
        break
    else:
        ("Şifreler uyuşmuyor! Lütfen rekrar deneyin!")

print("Kullanıcı Girişi")
hak = 3
while hak > 0:
    girilen_sifre = getpass.getpass("Şifrenizi girin: ")

    if girilen_sifre == sifre:
        print(f"Hoş Geldiniz, {ad}!")
        break
    else:
        hak -= 1
        ("Hatalı şifre! Tekrar deneyin!")
        if hak == 0:
            print("3 kez hatalı giriş yaptınız! Hesabınız kitlendi!")
            exit()