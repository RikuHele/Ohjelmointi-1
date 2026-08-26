import math

# Tehtävä 1

nimi = input("Hei, mikä on nimesi?\n")
print("\nTerve, " + nimi + "!")

# Tehtävä 2

sade = float(input("\nMikä on ympyrän säde?\n"))

print("Ympyrän pinta-ala on: ")
print(sade*sade*math.pi)

# Tehtävä 3

print("\nSeuraavaksi laskemme suorakulmion pinta-alan ja piirin.")
kanta = float(input("\nMikä on suorakulmion kanta?\n"))
korkeus = float(input("\nMikä on suorakulmion korkeus?\n"))

print("\nSuorakulmion pinta-ala on: ")
print(kanta*korkeus)

print("Suorakulmion piiri on: ")
print(kanta + kanta + korkeus + korkeus)

# Tehtävä 4

print("\nSeuraavaksi pyydän sinulta 3 kokonaislukua, josta lasketaan summa, tulo ja keskiarvo.\n")
numero1 = int(input("\nEnsimmäinen numero: \n"))
numero2 = int(input("\nToinen numero: \n"))
numero3 = int(input("\nJa vielä kolmas numero: \n"))

print("\nAntamiesi numeroiden summa on: ")
print(numero1 + numero2 + numero3)

print("\nAntamiesi numeroiden tulo on: ")
print(numero1 * numero2 * numero3)
print("\nAntamiesi numeroiden keskiarvo on: ")
print((numero1 + numero2 + numero3) / 3)

# Tehtävä 5

print("\nSeuraavaksi pyydän leivisköjä, nauloja ja luoteja. Nämä muunnetaan kilogrammoiksi ja grammoiksi.")

leiviskä = int(input("\nAnna leiviskät:\n"))
naula = int(input("\nAnna naulat:\n"))
luoti = float(input("\nAnna luodit:\n"))
# luoti floattina koska ainakin esimerkissä luoti ilmoitettu 13.5

luoteja = leiviskä * 20 * 32 + naula * 32 + luoti
# muutetaan kaikki luodeiksi niin on helppo laskea

gramma = luoteja * 13.3
# merkitään grammojen funktio, koska yksi luoti on 13,3g

kilogrammat = int(gramma // 1000) # // jotta saadaan kokonaisluku
grammat = gramma % 1000 # % jotta saadaan jakojäännös, eli ...g

print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kg ja {grammat:0.2f} g.")


# Tehtävä 6

print("\nSeuraavaksi ohjelma tulostaa täysin sattumanvaraisena 3-numeroisen koodin ja numerot on väliltä 1-9. Tulostaa myös 4-numeroisen koodin jonka numerot on väliltä 1-6.\n")

import random

koodi1 = random.randint(0, 999)

if koodi1 < 10:
    print("Koodisi on: 00" + str(koodi1))
elif koodi1 < 100:
    print("Koodisi on: 0" + str(koodi1))
else:
    print(f"Koodisi on: {koodi1} ")

koodi2 = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))

print(f"\nKoodisi on: {koodi2}")