
with open("ornek.txt","r",encoding="utf-8") as dosya:
    icerik = dosya.read()
    print(icerik)

with open("ornek.txt","w",encoding="utf-8") as dosya:
    dosya.write("Bu, yeni bir dosya yazısıdır.\n")

with open("ornek.txt","a",encoding="utf-8") as dosya:
    dosya.write("Bu, yeni eklenen satır.")