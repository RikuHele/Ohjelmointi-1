# Tehtävä 1

class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumäärä):
        Julkaisu.__init__(self, nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumäärä = sivumäärä

    def tulosta_tiedot(self):
        print(f'\nTeoksen nimi: {self.nimi}')
        print(f'Kirjoittajan nimi: {self.kirjoittaja}')
        print(f'Sivumäärä: {self.sivumäärä}')


class Lehti(Julkaisu):
    def __init__(self, nimi, päätoimittaja):
        Julkaisu.__init__(self, nimi)
        self.päätoimittaja = päätoimittaja

    def tulosta_tiedot(self):
        print(f'\nLehden nimi: {self.nimi}')
        print(f'Päätoimittajan nimi: {self.päätoimittaja}')

k1 = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)
l1 = Lehti('Aku Ankka', 'Aki Hyyppä')

k1.tulosta_tiedot()
l1.tulosta_tiedot()

# Tehtävä 2

class Auto:
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

class Sähköauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, kwh):
        Auto.__init__(self, rekisteritunnus, huippunopeus)
        self.kwh = kwh

class Polttomoottoriauto(Auto):
    def __init__(self, rekisteritunnus, huippunopeus, L):
        Auto.__init__(self, rekisteritunnus, huippunopeus)
        self.L = L

s1 = Sähköauto('ABC-15', 180, 52.5)
p1 = Polttomoottoriauto('ACD-123', 165, 32.3)

s1.kiihdytä(73)
p1.kiihdytä(92)

s1.kulje(3)
p1.kulje(3)

print(f'\nSähköauton kuljettu matka (73 km/h): {s1.kuljettu_matka} km')
print(f'Polttomoottoriauton kuljettu matka (92 km/h): {p1.kuljettu_matka} km')