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
with open(r"C:\Users\Domc\Desktop\infó\verseny\2025.03\Lakosok.csv", "r", encoding="utf8") as file:
    fejlec = file.readline().strip().split(";")  # Az első sor (oszlopnevek)
    lakosok = [Lakos(*sor.strip().split(";")) for sor in file]

# Ellenőrzés: kiírunk néhány sort
for lakos in lakosok[:5]:
    print(lakos)