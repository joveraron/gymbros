import szolgaltatasok
import epuletek
import lakosok
import koltsegek_allapotok
import projektek
import random

'''for szolgaltatas in szolgaltatasok.szolgaltatasok:
    print(szolgaltatas.nev)'''

helyes = False
while helyes == False:
    e_elegedettseg = int(input('Adja meg a lakosok elvárt minimum elégedettségét 0 és 80 között: '))
    if 0 <= e_elegedettseg <= 80:
        helyes = True
    else:
        print('A szám nem megfelelő')

elegedettseg = e_elegedettseg + 20
penzkeret = int(input('Adja meg a kezdő pénzkeretet: '))
hossza = int(input('Adja meg a szimuláció hosszát fordulókban:'))
jelen = projektek.Ido(2025, 4, 1)
meddigtart = []
fajlba = []
listaba = []

print(jelen.honap)

while penzkeret > 0 and elegedettseg >= e_elegedettseg and hossza > 0:
    parancs = input('írjon be egy parancsot. A parancsok listáját a "parancsok" beírásával hívhatja elő: ')

    if parancs == "parancsok":
        print('epulet - Új épület építése')
        print('ujszolgaltatas - Új szolgáltatás bevezetése')
        print('szolgaltatastorlese - Szolgáltatás törlése')

    elif parancs == "epulet":
        f = open("Épületek.csv", "a", encoding="utf8")
        alma = epuletek.Epulet(int(input('Adja meg az épület azonosítóját: ')), input('Adja meg az épület nevét: '), input('Adja meg az épület típusát: '), int(input('adja meg az építés évét: ')), int(input('Adja meg az épület hasznos területét: ')))
        f.write(f"{alma.azon};{alma.nev};{alma.tipus};{alma.epiteseve};{alma.hasznosterulet}\n")
        epuletek.epuletek.append(alma)
        projektek.ujprojekt(alma.nev, alma.hasznosterulet, jelen)
        print(projektek.projektek[6])
        penzkeret = 0

    elif parancs == "ujszolgaltatas":
        alma = szolgaltatasok.Szolgaltatas(int(input('Adja meg az szolgáltatás azonosítóját: ')), input('Adja meg az szolgáltatás nevét: '), input('Adja meg az szolgáltatás típusát: '), int(input('adja meg az épület azonosítóját, amelyben a szolgáltatás található: ')))
        z = open("Szolgáltatások.csv", "a", encoding="utf8")
        z.write(f"{alma.azon};{alma.nev};{alma.tipus};{alma.Ep_azon}\n")
        bevagyki = input('adja meg hogy a szolgáltatás a város számára bevétel(B) vagy kiadás(K): ')
        helyes = False
        while helyes == False:
            if bevagyki == 'bevétel' or bevagyki == 'b' or bevagyki == 'B' or bevagyki == 'kiadás' or bevagyki == 'k' or bevagyki == 'k':
                if bevagyki == 'bevétel' or bevagyki == 'b' or bevagyki == 'B':
                    bevetel = int(input('Adja meg mennyi bevételt termeljen a szolgáltatás havonta: '))
                    koltsegek_allapotok.koltsegek.append(bevetel)
                    helyes = True
                else:
                    bevetel = -1 * int(input('Adja meg mennyi kiadás legyen a szolgáltatás havonta: '))
                    koltsegek_allapotok.koltsegek.append(bevetel)
                    helyes = True
        elegedettseg += random.randint(5, 15)
        print(elegedettseg)

    elif parancs == "szolgaltatastorlese":
        torles = int(input('Adja meg a törölni kívánt szolgáltatás azonosítóját: '))
        i = 0
        hanyadik = -1

        for szolgaltatas in szolgaltatasok.szolgaltatasok:
            if szolgaltatas.azon == torles:
                hanyadik = i
            i += 1
        szolgaltatasok.szolgaltatasok.pop(hanyadik)

        szolgaltatastorles = open("Szolgáltatások.csv", "w", encoding="utf8")

        for szolgaltatas in szolgaltatasok.szolgaltatasok:
            szolgaltatastorles.write(f"{szolgaltatas.azon};{szolgaltatas.nev};{szolgaltatas.tipus};{szolgaltatas.Ep_azon}\n")
        penzkeret = 0
        
        elegedettseg -= random.randint(5, 15)
        print(elegedettseg)

'''def main():
    '''