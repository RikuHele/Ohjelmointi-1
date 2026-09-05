import random

# Tehtävä 1

noppien_määrä = int(input("Anna noppien määrä:\n"))

summa = 0

for n in range(noppien_määrä):
    noppa = random.randint(1,6)
    summa = summa + noppa

print(f'\nSilmälukujen summa on: {summa}.')

# Tehtävä 2

luvut = []

while True:
    lukujono = input("Anna luku:\n")

    if lukujono == "":
        break

    luku = float(lukujono)
    luvut.append(luku)

luvut.sort(reverse=True)

for luku in luvut[:5]:
    print(luku)

# Tehtävä 3

luku3 = int(input("Anna kokonaisluku:\n"))

alkuluku = True

if luku3 < 2:
    alkuluku = False

for a in range(2, luku3):
    if luku3 % a == 0:
        alkuluku = False

if alkuluku:
    print("\nLuku on alkuluku.")
else:
    print("\nLuku ei ole alkuluku.")

# Tehtävä 4

kaupungit = []

for k in range(5):
    kaupunki = input("Anna kaupungin nimi:\n")
    kaupungit.append(kaupunki)

print("\nTässä kaupungit:\n")

for kaupunki in kaupungit:
    print(kaupunki)