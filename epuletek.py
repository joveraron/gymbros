class Lakos:
    def __init__(self, azon, nev, tipus, epiteseve, hasznosterulet):
        self.azon = int(azon)
        self.nev = nev
        self.tipus = tipus
        self.epiteseve = int(epiteseve)
        self.hasznosterulet = int(hasznosterulet)

    def __repr__(self):
        return f"{self.azon}: {self.nev}, {self.tipus}, {self.epiteseve}, {self.hasznosterulet}"

# Adatok beolvasása fájlból
with open(r"C:\Users\Domc\Desktop\infó\verseny\2025.03\Épületek.csv", "r", encoding="utf8") as file:
    fejlec = file.readline().strip().split(";")  # Az első sor (oszlopnevek)
    epuletek = [Lakos(*sor.strip().split(";")) for sor in file]

# Ellenőrzés: kiírunk néhány sort
for lakos in epuletek[:5]:
    print(lakos)