# importteja

from luokat.player import Player
from huoneet_esineet_luonti import kaupunki, metsä, joki, leiripaikka, kauppa, metroasema, keskusta, pyörävarasto, korjaamo, pyörätie, tukikohta
from huoneet_esineet_luonti import lapio, lamppu, kirves, jakoavain, polkupyörä

# --- Pelin tallennus --- #

def tallenna_peli(pelaaja):
    # "w" = write, vanha tallennus korvataan uudella
    with open("tallennus.txt", "w") as tiedosto:
        tiedosto.write(pelaaja.nimi + "\n")
        tiedosto.write(str(pelaaja.ikä) + "\n") # write tarvitsee merkkijonon joten int muutetaan str
        tiedosto.write(pelaaja.sijainti.nimi + "\n")
        tiedosto.write(str(pelaaja.raha) + "\n") # write tarvitsee merkkijonon joten int muutetaan str
        for tavara in pelaaja.reppu: # käydään kaikki repun esine-oliot läpi
            tiedosto.write(tavara.nimi + "\n") # tallennetaan vain esineen nimi ei itse oliota

# --- Pelin lataaminen --- #

def lataa_peli():
    try:
        with open("tallennus.txt", "r") as tiedosto: # "r" = read, eli luetaan tiedostolta
            rivit = tiedosto.readlines() # muutetaan tiedoston rivit listaksi
            nimi = rivit[0].strip() # strip poistaa turhat välilyönnit, rivinvaihdot tms
            ikä = int(rivit[1].strip()) # muutetaan takaisin int muotoon str:stä
            sijainti = rivit[2].strip()
            raha = int(rivit[3].strip()) # muutetaan takaisin int muotoon str:stä

            repun_tavarat = rivit[4:] # indeksistä 4 eteenpäin ovat repun tavaroita
            tallennettu_reppu = []

            esineet = { # muuttaa tiedostosta luetun esineen nimen takaisin Esine-olioksi
                "Lapio": lapio,
                "Lamppu": lamppu,
                "Kirves": kirves,
                "Jakoavain": jakoavain,
                "Polkupyörä": polkupyörä
            }

            huoneet = { # muuttaa tiedostosta luetun sijainnin nimen takaisin Huone-olioksi
                "Kaupunki": kaupunki, # esim. tiedostossa "Kaupunki" on key ja se muutetaan valueksi eli olio kaupunki
                "Metsä": metsä,
                "Joki": joki,
                "Leiripaikka": leiripaikka,
                "Kauppa": kauppa,
                "Metroasema": metroasema,
                "Keskusta": keskusta,
                "Pyörävarasto": pyörävarasto,
                "Korjaamo": korjaamo,
                "Pyörätie": pyörätie,
                "Tukikohta": tukikohta
            }

            for tavara in repun_tavarat:
                tavara = tavara.strip()
                tallennettu_reppu.append(esineet[tavara])

            tallennettu_pelaaja = Player(nimi, ikä, huoneet[sijainti]) # luodaan tallennustiedoston tietojen perustella uusi Player-olio
            tallennettu_pelaaja.raha = raha # palautetaan tallannettu raha ja reppu
            tallennettu_pelaaja.reppu = tallennettu_reppu

            return tallennettu_pelaaja # palautetaan valmis pelaaja-olio tästä lataa_peli funktiosta

    except FileNotFoundError:
        print("\nTallennettua peliä ei löytynyt")