import random
import epuletek
import szolgaltatasok

allapotok = []

for epulet in epuletek.epuletek:
    allapotok.append(random.randint(1, 5))

koltsegek = []

for szolgaltatas in szolgaltatasok.szolgaltatasok:
    if szolgaltatas.azon == 4 or 6 or 7 or 8 or 10 or 11 or 12 or 13 or 14 :
        koltsegek.append(-1 * random.randint(1000000, 5000000))
    else:
        koltsegek.append(random.randint(1000000, 4000000))