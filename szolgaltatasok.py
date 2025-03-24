class Szolgaltatas:
    def __init__(self, azon, nev, tipus, Ep_azon):
        self.azon = int(azon)
        self.nev = nev
        self.tipus = tipus
        self.Ep_azon = int(Ep_azon)

    def __repr__(self):
        return f"{self.azon}: {self.nev}, {self.tipus}, {self.Ep_azon}"

# Adatok beolvasása fájlból
szolgaltatasok_fajl = open(r"Szolgáltatások.csv", "r", encoding="utf8")

fejlec = szolgaltatasok_fajl.readline().strip().split(";")  # Az első sor (oszlopnevek)
szolgaltatasok = []

for sor in szolgaltatasok_fajl:
    szolgaltatasok.append(Szolgaltatas(*(sor.strip().split(";"))))

'''for szolgaltatas in szolgaltatasok:
    print(szolgaltatas.azon)'''
