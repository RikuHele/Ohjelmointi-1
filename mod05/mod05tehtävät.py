# Tehtävä 1

luku = 1

while luku <= 1000:
    if luku % 3 == 0:
        print(luku)

    luku = luku + 1

# Tehtävä 2

tuumamäärä = float(input("Anna minulle tuumamäärä:\n"))

while tuumamäärä >= 0:
    sentit = tuumamäärä * 2.54
    print(f'\nTuumamääräsi senttimetreinä: {sentit:0.2f}')
    tuumamäärä = float(input("Anna minulle tuumamäärä:\n"))

print("\nOhjelma lopetettu, annoit negatiivisen luvun.")

# Tehtävä 3

lukujono = input("Anna luku:\n")

pienin = float(lukujono)
suurin = float(lukujono)

while True:
    lukujono = input("Anna luku (tyhjä vastaus lopettaa toiminnon):\n")

    if lukujono == "":
        break

    luku3 = float(lukujono)

    if luku3 < pienin:
        pienin = luku3

    if luku3 > suurin:
        suurin = luku3

print(f'Pienin luku oli: {pienin}.')
print(f'Suurin luku oli: {suurin}.')

# Tehtävä 4

import random

arpa = random.randint(1, 10)
vastaus = int(input("\nArvaa tietokoneen arpoma luku 1-10:\n"))

while vastaus != arpa:
    if arpa < vastaus:
        print("\nLiian suuri arvaus")

    elif arpa > vastaus:
        print("\nLiian pieni arvaus")

    vastaus = int(input("\nArvaa tietokoneen arpoma luku 1-10:\n"))

print("\nVastauksesi on oikein!")

# Tehtävä 5

kokeilut = 0

while kokeilut < 5:
    käyttäjätunnus = input("\nAnna käyttäjätunnus:\n")
    salasana = input("\nAnna salasana:\n")

    kokeilut = kokeilut + 1

    if käyttäjätunnus == "python" and salasana == "rules":
        print("\nTervetuloa.")
        break
    
    if käyttäjätunnus != "python":
        print("\nVäärä käyttäjätunnus.")

    if salasana != "rules":
        print("\nVäärä salasana.")

    if kokeilut == 5 and (käyttäjätunnus != "python" or salasana != "rules"):
        print("\nPääsy evätty.")

        