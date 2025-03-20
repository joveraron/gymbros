class Lakos:
    def __init__(self, azon, nev, tipus, Ep_azon):
        self.azon = int(azon)
        self.nev = nev
        self.tipus = tipus
        self.Ep_azon = int(Ep_azon)

    def __repr__(self):
        return f"{self.azon}: {self.nev}, {self.tipus}, {self.Ep_azon}"

# Adatok beolvasása fájlból
with open(r"C:\Users\Domc\Desktop\infó\verseny\2025.03\Szolgáltatások.csv", "r", encoding="utf8") as file:
    fejlec = file.readline().strip().split(";")  # Az első sor (oszlopnevek)
    szolgaltatasok = [Lakos(*sor.strip().split(";")) for sor in file]

# Ellenőrzés: kiírunk néhány sort
for lakos in szolgaltatasok[:5]:
    print(lakos)