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
        self.honap = int(honap)
        self.nap = int(nap)

# Adatok beolvasása fájlból
projekt_fajl = open(r"Projektek.csv", "r", encoding="utf8")

projektek = []
kezdoevek = []
befevek = []
meddigtart = []

for sor in projekt_fajl:
    projektek.append(Projekt(*(sor.strip().split(";"))))
    
for projekt in projektek:
    kezdoevek.append(Ido(*((projekt.kezdodatum).strip().split("."))))
    befevek.append(Ido(*((projekt.befejezodatum).strip().split("."))))

i = 0

for projekt in projektek:
    if kezdoevek[i].ev < befevek[i].ev:
        alma = 12 - kezdoevek[i].honap + befevek[i].honap
        meddigtart.append(alma)
    else:
        alma = befevek[i].honap - kezdoevek[i].honap
        meddigtart.append(alma)
    i += 1