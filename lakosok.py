class Lakos:
    def __init__(self, azon, nev, szuletesiev, foglalkozas, lakohely):
        self.azon = int(azon)
        self.nev = nev
        self.szuletesiev = int(szuletesiev)
        self.foglalkozas = foglalkozas
        self.lakohely = int(lakohely)

    def __repr__(self):
        return f"{self.azon}: {self.nev}, {self.szuletesiev}, {self.foglalkozas}, {self.lakohely}"

# Adatok beolvasása fájlból
lakosok_fajl = open(r"Lakosok.csv", "r", encoding="utf8")

fejlec_lakosok = lakosok_fajl.readline().strip().split(";")  # Az első sor (oszlopnevek)
lakosok = []

for sor in lakosok_fajl:
    lakosok.append(Lakos(*(sor.strip().split(";"))))

for lakos in lakosok:
    print(lakos.azon)

'''--------------------------------------------------------------Szolgaltatasok------------------------------------------------------------------------------------------'''

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

for szolgaltatas in szolgaltatasok:
    print(szolgaltatas.azon)

'''--------------------------------------------------------------Epuletek------------------------------------------------------------------------'''

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
    epuletek.append(Szolgaltatas(*(sor.strip().split(";"))))

for epulet in epuletek:
    print(epulet.azon)
