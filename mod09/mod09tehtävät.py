# Tehtävä 1

class Auto1:
    def __init__(self, rekisteritunnus, huippunopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus


auto1 = Auto1("ABC-123", 142)

print(f'{auto1.rekisteritunnus} / {auto1.huippunopeus} km/h')

# Tehtävä 2

class Auto1:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

auto1 = Auto1("ABC-123", 142, 0)

auto1.kiihdytä(30)
auto1.kiihdytä(70)
auto1.kiihdytä(50)
print(f'\nKiihdytyksen jälkeen auton nopeus on: {auto1.nopeus} km/h')

auto1.kiihdytä(-200)
print(f'Hätäjarrutuksen jälkeen nopeus on: {auto1.nopeus} km/h')

# Tehtävä 3

class Auto1:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus, kuljettu_matka):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.nopeus*tuntimäärä

auto3 = Auto1("ABC-123", 142, 60, 2000)


auto3.kulje(1.5)

print(f'\nAuto kulki yhteensä: {auto3.kuljettu_matka} km')

# Tehtävä 4

import random

class Auto1:
    def __init__(self, rekisteritunnus, huippunopeus, nopeus = 0, kuljettu_matka = 0):
        self.rekisteritunnus = rekisteritunnus
        self.huippunopeus = huippunopeus
        self.nopeus = nopeus
        self.kuljettu_matka = kuljettu_matka

    def kiihdytä(self, nopeuden_muutos):
        self.nopeus += nopeuden_muutos

        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus

        if self.nopeus < 0:
            self.nopeus = 0

    def kulje(self, tuntimäärä):
        self.kuljettu_matka += self.nopeus*tuntimäärä

autot = []

kilpailu_loppui = False

for numero in range (1, 11):
    autot.append(Auto1(f"ABC-{numero}", random.randint(100, 200)))

while True:
    for auto in autot:
        auto.kiihdytä(random.randint(-10, 15))
        auto.kulje(1)

    for auto in autot:
        if auto.kuljettu_matka >= 10000:
            kilpailu_loppui = True
            break

    if kilpailu_loppui == True:
        break

print("")
print('Rekisteritunnus | Huippunopeus (km/h) | Nopeus (km/h) | Kuljettu matka (km)')
print('---------------------------------------------------------------------------')
for auto in autot:
    print(f'{auto.rekisteritunnus:<15} | {auto.huippunopeus:<19} | {auto.nopeus:<13} | {auto.kuljettu_matka:<15}')

