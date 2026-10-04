class Player:
    def __init__(self, nimi, ikä, sijainti):
        # alustetaan Player olion ominaisuudet
        self.nimi = nimi
        self.ikä = ikä
        self.sijainti = sijainti
        self.raha = 0
        self.reppu = []

    def liiku(self, uusi_sijainti):
        # metodi vaihtaa pelaajan sijainnin uuteen huone-olioon
        self.sijainti = uusi_sijainti

    def kerää_esine(self, esine):
        # varmistetaan, ettei samaa Esine-oliota lisätä reppuun kahdesti
        if esine in self.reppu:
            print("\nSinulla on jo tämä tavara repussasi")
        else:
            self.reppu.append(esine)