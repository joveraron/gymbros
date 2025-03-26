def epites():
    f = open("Épületek.csv", "a", encoding="utf8")
    alma = epuletek.Epulet(int(input('Adja meg az épület azonosítóját: ')), input('Adja meg az épület nevét: '), input('Adja meg az épület típusát: '), int(input('adja meg az építés évét: ')), int(input('Adja meg az épület hasznos területét: ')))
    f.write(f"{alma.azon};{alma.nev};{alma.tipus};{alma.epiteseve};{alma.hasznosterulet}\n")
    epuletek.epuletek.append(alma)
        
    
    
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

for epulet in epuletek:
    print(epulet.azon)
