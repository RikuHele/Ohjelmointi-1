# Sanapeli

# --- Importit --- #

import os

# --- Pelaajan ikä ja nimi --- #

player_name = input("\nTervetuloa peliin. Kerro nimesi:\n")
player_age = int(input(f"\nHauska tavata {player_name}! Kuinka vanha olet?\n"))
# nyt pelaajan ikä ja nimi tallennetaan muuttujiin

if player_age < 12:
    print("\nPelin ikäraja on 12v, peli sammutetaan.")
    exit()

# --- Listoja --- #

reppu = []

# --- Funktioita --- #

def tyhjennä_ruutu():
    os.system("clear")

def aloita_peli():
    print(f'\nAloitetaan peli, onnea matkaan {player_name}!')
    
def pelin_ohjeet():
    print(f'\nTässä pelin ohjeet:')
    print('\nPelin tavoite on läpäistä peli jotain reittiä pitkin ja valinnat ovat täysin sinun käsissäsi.')
    print('Pelissä on useampi (3kpl) reitti, jota pitkin pelin voi läpäistä. Kestävän kehityksen teema on otettu tässä huomioon.')
    print('Päävalikossa voit valita asioita, joita voit ottaa mukaan reppuusi matkan ajaksi. Voit tarvita näitä asioita matkan varrella :).')
    print('Pelissä on yhteensä erilaisia tiloja 11 kappaletta. Näin ollen, sinulle jää reippaasti valinnanvaraa reitillesi.')
    print('Toivotan sinulle onnea matkaasi valitsemallasi reitillä! Nähdään perillä.')

def lisää_reppu():
    print('\nTässä lista erilaisista asioita mitä on saatavilla lisätä reppuusi:')
    print('\n1. Lapio')
    print('2. Lamppu')
    print('3. Kirves')
    print('4. Jakoavain')
    print('5. 100€ käteistä rahaa')
    print('6. Olen valmis siirtymään pois tavaravalinnoista.')

    while True:
        sisältö = input('\nMitä asioita haluaisit lisätä reppuusi? Vastaa (1-6):\n')

        if sisältö == "1":
            reppu.append("Lapio")
            print("Lapio lisätty.")
        elif sisältö == "2":
            reppu.append("Lamppu")
            print("Lamppu lisätty.")
        elif sisältö == "3":
            reppu.append("Kirves")
            print("Kirves lisätty.")
        elif sisältö == "4":
            reppu.append("Jakoavain")
            print("Jakoavain lisätty")
        elif sisältö == "5":
            reppu.append("100€ käteistä rahaa")
            print("100€ käteistä rahaa lisätty.")
        elif sisältö == "6":
            break
        else:
            print("\nValitse 1-6. Kokeillaan uudestaan.")

def näytä_reppu():
    if reppu == []:
        print('\nReppusi on vielä tyhjä')

    else:
        print('\n=== Reppusi sisältö ===\n')
        for tavara in reppu:
            print(tavara)

def krediitit():
    print('\nTässä tietoja pelin tekijästä:\n')
    print('Nimi: Riku Helenius')
    print('Ikä: 21v, syntynyt vuonna 2005')
    print('Ala: Opiskelee tieto- ja viestintätekniikkan insinööriksi')
    print('Mielenkiinnon kohteita: Ollut aina kiinnostunut ohjelmoinnista ja urheilusta')

def paina_enter():
    input("\nPaina enter kun olet valmis.")

def lopeta_peli():
    print('\nLopetetaan peli.')
    return True

# --- Päävalikko --- #

print(f"\nTervetuloa pelaamaan peliä {player_name}! ")

while True:
    print("\n=== Päävalikko ===")
    print("1. Ohjeet")
    print("2. Lisää tavaroita reppuusi")
    print("3. Reppusi sisältö")
    print("4. Krediitit")
    print("5. Aloita peli")
    print("6. Lopeta")

    valinta = input("\nValitse vaihtoehto (1-5):\n")

    if valinta == "1":
        pelin_ohjeet()
        paina_enter()
        tyhjennä_ruutu()

    elif valinta == "2":
        lisää_reppu()
        paina_enter()
        tyhjennä_ruutu()

    elif valinta == "3":
        näytä_reppu()
        paina_enter()
        tyhjennä_ruutu()

    elif valinta == "4":
        krediitit()
        paina_enter()
        tyhjennä_ruutu()

    elif valinta == "5":
        aloita_peli()
        paina_enter()
        tyhjennä_ruutu()
        break

    elif valinta == "6":
        if lopeta_peli():
            exit()

    else:
        print("\nVäärä valinta, se ei ollut vaihtoehtona.")
        tyhjennä_ruutu()