class Epulet:
    def __init__(self, azon, nev, tipus, epiteseve, hasznosterulet):
        self.azon = int(azon)
        self.nev = nev
        self.tipus = tipus
        self.epiteseve = int(epiteseve)
        self.hasznosterulet = int(hasznosterulet)

    def __repr__(self):
        return f"{self.azon}: {self.nev}, {self.tipus}, {self.epiteseve}, {self.hasznosterulet}"

# Adatok beolvasása fájlból
epuletek_fajl = open(r"Épületek.csv", "r", encoding="utf8")

fejlec = epuletek_fajl.readline().strip().split(";")  # Az első sor (oszlopnevek)
epuletek = []

for sor in epuletek_fajl:
    epuletek.append(Epulet(*(sor.strip().split(";"))))

'''for epulet in epuletek:
    print(epulet.azon)'''
