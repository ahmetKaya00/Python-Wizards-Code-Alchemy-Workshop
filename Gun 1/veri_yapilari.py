meyveler = ["Elma","Armut","Muz","Kiraz"]
print(meyveler)

print(meyveler[0])
print(meyveler[-1])

meyveler[1] = "Karpuz"
print(meyveler)

meyveler.append("Çilek")
meyveler.insert(1,"Portakal")
meyveler.remove("Muz")
print(meyveler)

for meyve in meyveler:
    print(meyve)

demetler = ("elma","Armut","Muz")

print(demetler)
#demetler[1] = "Karpuz"
#demetler.append("Elma")
print(demetler)

ogrenci = {
    "ad": "Cerensu",
    "soyad": "Karameşe",
    "yas": 25
}

print(ogrenci["ad"])

ogrenci["sehir"] = "İstanbul"

renkler = {"Kırmızı","Mavi","Yeşil","Sarı","Mavi"}
print(renkler)