class Arac:
    def heraket_et(self):
        print("Araç hareket ediyor....")

class Araba(Arac):
    def __init__(self,marka):
        self.marka = marka



arac = Araba("Mercedes")
arac.heraket_et()