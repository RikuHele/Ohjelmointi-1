# Tehtävä 1

class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin_kerros = alin_kerros
        self.ylin_kerros = ylin_kerros
        self.nykyinen_kerros = alin_kerros

    def siirry_kerrokseen(self, annettu_kerros):
        
        while self.nykyinen_kerros < annettu_kerros:
            self.kerros_ylös()

        while self.nykyinen_kerros > annettu_kerros:
            self.kerros_alas()

    def kerros_ylös(self):
        self.nykyinen_kerros += 1
        print(f'Hissi on nyt kerroksessa {self.nykyinen_kerros}')

    def kerros_alas(self):
        self.nykyinen_kerros -= 1
        print(f'Hissi on nyt kerroksessa {self.nykyinen_kerros}')

hissi = Hissi(1,10)
hissi.siirry_kerrokseen(5)
hissi.siirry_kerrokseen(hissi.alin_kerros)

# Tehtävä 2

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.hissit = []
        for _ in range (hissien_määrä):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohde_kerros)

talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 7)
talo.aja_hissiä(2,8)
talo.aja_hissiä(3, 5)

# Tehtävä 3

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_määrä):
        self.hissit = []
        for _ in range (hissien_määrä):
            self.hissit.append(Hissi(alin_kerros, ylin_kerros))

    def aja_hissiä(self, hissin_numero, kohde_kerros):
        hissi = self.hissit[hissin_numero - 1]
        hissi.siirry_kerrokseen(kohde_kerros)

    def palohälytys(self):
        for hissi in self.hissit:
            hissi.siirry_kerrokseen(hissi.alin_kerros)

talo = Talo(1, 10, 3)
talo.aja_hissiä(1, 7)
talo.aja_hissiä(2,8)
talo.aja_hissiä(3, 5)
talo.palohälytys()

# Tehtävä 4

#from mod09.mod09tehtävät import Auto1 / tämä ei toimi joten kopioin vanhasta tehtävästä.
import random
import time

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

class Kilpailu:
    def __init__(self, kilpailun_nimi, pituus_km, osallistuvat_autot):
        self.kilpailun_nimi = kilpailun_nimi
        self.pituus_km = pituus_km
        self.osallistuvat_autot = osallistuvat_autot

    def tunti_kuluu(self):
        for auto in self.osallistuvat_autot:
            auto.kiihdytä(random.randint(-10, 15))
            auto.kulje(1)

    def tulosta_tilanne(self):
        print("")
        print('Rekisteritunnus | Huippunopeus (km/h) | Nopeus (km/h) | Kuljettu matka (km)')
        print('---------------------------------------------------------------------------')
        for auto in self.osallistuvat_autot:
            print(f'{auto.rekisteritunnus:<15} | {auto.huippunopeus:<19} | {auto.nopeus:<13} | {auto.kuljettu_matka:<15}')


    def kilpailu_ohi(self):
        for auto in self.osallistuvat_autot:
            if auto.kuljettu_matka >= self.pituus_km:
                return True

        return False

autot = []

for numero in range (1, 11):
    autot.append(Auto1(f"ABC-{numero}", random.randint(100, 200)))

kilpailu = Kilpailu('Suuri romuralli', 8000, autot)

tunnit = 0

while True:
    kilpailu.tunti_kuluu()
    tunnit += 1

    if tunnit % 10 == 0:
        kilpailu.tulosta_tilanne()
        time.sleep(5)

    if kilpailu.kilpailu_ohi():
        break

kilpailu.tulosta_tilanne()