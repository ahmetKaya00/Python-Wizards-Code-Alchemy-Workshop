class Araba:
    def __init__(self, marka,model,yil):
        self.marka = marka
        self.model = model
        self.yil = yil

    def arac_calistir(self):
        print(f"{self.marka}Araba şuan çalışıyor....")



arac = Araba("Audi","A5",2024)
print(arac.marka)
arac.arac_calistir()