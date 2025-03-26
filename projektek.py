class Projekt:
    def __init__(self, azon, nev, koltseg, kezdodatum, befejezodatum):
        self.azon = int(azon)
        self.nev = nev
        self.koltseg = int(koltseg)
        self.kezdodatum = kezdodatum
        self.befejezodatum = befejezodatum

    def __repr__(self):
        return f"{self.azon}: {self.nev}, {self.koltseg}, {self.kezdodatum}, {self.befejezodatum}"

class Ido:
    def __init__(self, ev, honap, nap):
        self.ev = int(ev)
        self.honap = int (honap)
        self.nap = int(nap)

# Adatok beolvasása fájlból
projekt_fajl = open(r"Projekt.csv", "r", encoding="utf8")

fejlec = projekt_fajl.readline().strip().split(";")  # Az első sor (oszlopnevek)
projektek = []

for sor in projekt_fajl:
    projektek.append(Projekt(*(sor.strip().split(";"))))
    
for projekt in projektek:
    Ido(*((projekt.kezdodatum).strip().split(".")))