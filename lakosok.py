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

'''for lakos in lakosok:
    print(lakos.azon)'''