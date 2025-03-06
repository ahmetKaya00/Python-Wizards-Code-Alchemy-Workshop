def kullanici_kayit(ad,yas):
    if yas < 18:
        return "Üzgünüm, 18 yaşından küçükler kayıt olamaz!"
    return f"Kullanıcı {ad} başarıyla kaydedildi!"

def kullanici_girisi(ad, sifre, kayitli_sifre):
    if sifre == kayitli_sifre:
        return f"Hoş geldiniz, {ad}"
    return "Hatalı Şifre!"