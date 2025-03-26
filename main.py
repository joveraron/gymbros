import szolgaltatasok
import epuletek
import lakosok
import koltsegek_allapotok

'''for szolgaltatas in szolgaltatasok.szolgaltatasok:
    print(szolgaltatas.nev)'''

helyes = False
while helyes == False:
    elegedettseg = int(input('Adja meg a lakosok elégedettségét 0 és 100 között: '))
    if 0 <= elegedettseg <= 100:
        helyes = True
    else:
        print('A szám nem megfelelő')

penzkeret = int(input('Adja meg a kezdő pénzkeretet: '))

while penzkeret > 0 and elegedettseg > 0:
    parancs = input('írjon be egy parancsot. A parancsok listáját a "parancsok" beírásával hívhatja elő: ')

    if parancs == "parancsok":
        print('epulet - Új épület építése')
        print('ujszolgaltatas - Új szolgáltatás bevezetése')
        print('szolgaltatastorlese - Szolgáltatás törlése')

    elif parancs == "epulet":
        f = open("Épületek.csv", "a", encoding="utf8")
        '''alma = epuletek.Epulet(int(input('Adja meg az épület azonosítóját: ')), input('Adja meg az épület nevét: '), input('Adja meg az épület típusát: '), int(input('adja meg az építés évét: ')), int(input('Adja meg az épület hasznos területét: ')))'''
        alma = epuletek.Epulet(int(1), 'alma', 'banán', int(1980), int(193))
        f.write(f"{alma.azon};{alma.nev};{alma.tipus};{alma.epiteseve};{alma.hasznosterulet}\n")
        epuletek.epuletek.append(alma)
        penzkeret = 0

    elif parancs == "ujszolgaltatas":
        '''alma = szolgaltatasok.Szolgaltatas(int(input('Adja meg az szolgáltatás azonosítóját: ')), input('Adja meg az szolgáltatás nevét: '), input('Adja meg az szolgáltatás típusát: '), int(input('adja meg az épület azonosítóját, amelyben a szolgáltatás található: ')))'''
        alma = szolgaltatasok.Szolgaltatas(int(1), 'alma', 'banán', int(1980))
        z = open("Szolgáltatások.csv", "a", encoding="utf8")
        z.write(f"{alma.azon};{alma.nev};{alma.tipus};{alma.Ep_azon}\n")
        penzkeret = 0

    elif parancs == "szolgaltatastorlese":
        torles = int(input('Adja meg a törölni kívánt szolgáltatás azonosítóját: '))
        i = 0
        '''for lakos in lakosok.lakosok:
            print(lakosok.lakosok[i])
            i += 1
        lakosok.lakosok[i.nev] = "torolt"'''
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

'''def main():
    '''