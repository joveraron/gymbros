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

f = open("Épületek.csv", "a", encoding="utf8")
'''alma = epuletek.Epulet(int(input('Adja meg az épület azonosítóját: ')), input('Adja meg az épület nevét: '), input('Adja meg az épület típusát: '), int(input('adja meg az építés évét: ')), int(input('Adja meg az épület hasznos területét: ')))'''
alma = epuletek.Epulet(int(1), 'alma', 'banán', int(1980), int(193))
f.write(f"{alma.azon};{alma.nev};{alma.tipus};{alma.epiteseve};{alma.hasznosterulet}\n")
epuletek.epuletek.append(alma)

'''alma = .Epulet(int(input('Adja meg az szolgáltatás azonosítóját: ')), input('Adja meg az szolgáltatás nevét: '), input('Adja meg az szolgáltatás típusát: '), int(input('adja meg az épület azonosítóját, amelyben a szolgáltatás található: ')))'''
alma = szolgaltatasok.Szolgaltatas(int(1), 'alma', 'banán', int(1980))
z = open("Szolgáltatások.csv", "a", encoding="utf8")
z.write(f"{alma.azon};{alma.nev};{alma.tipus};{alma.Ep_azon}\n")

torles = input('Adja meg a törölni kívánt szolgáltatás azonosítóját: ')
i = 0
while lakosok.lakosok[i] != torles:
    i += 1
    print(lakosok.lakosok[i])
lakosok.lakosok[i.nev] = "torolt"
'''def main():
    '''








