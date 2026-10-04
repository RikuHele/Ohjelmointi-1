# Sanapeli

# --- Importit --- #

import os
from luokat.player import Player
from huoneet_esineet_luonti import kaupunki, metsä, joki, leiripaikka, kauppa, metroasema, keskusta, pyörävarasto, korjaamo, pyörätie, tukikohta
from huoneet_esineet_luonti import lapio, lamppu, kirves, jakoavain, polkupyörä
from tallennus import tallenna_peli, lataa_peli

# --- Luokkia --- #

# luokat ovat luokka kansiossa

# --- Esineiden luonti ja Huoneiden luonti --- #

# tehty erillisessä huoneet_esineet_luonti tiedostossa

# --- Pelin esittely --- #

def pelin_esittely():
    with open("intro.txt", "r") as tiedosto:
        print(tiedosto.read())

pelin_esittely()

# --- Pelin tallennus ja lataus --- #

# tallennus ja lataus ovat erillisessä tallennus tiedostossa

# --- Uusi peli / Lataa peli --- #
# --- Samalla myös pelaajan luominen --- #

while True: # pidetään valikko käynnissä, kunnes break suoritetaan
    print("\n1. Uusi peli")
    print("2. Lataa peli")

    valinta = input("\nValitse (1-2):\n")

    if valinta == "1":
        player_name = input("\nTervetuloa peliin. Kerro nimesi:\n")
        player_age = int(input(f"\nHauska tavata {player_name}! Kuinka vanha olet?\n"))
        
        # nyt pelaajan ikä ja nimi tallennetaan muuttujiin

        if player_age < 12:
            print("\nPelin ikäraja on 12v, peli sammutetaan.")
            exit()
            # jos pelaaja on alle 12v, niin peli sammuu itsekseen'
        
        pelaaja = Player(player_name, player_age, kaupunki) # luodaan pelaaja-olio
        break

    elif valinta == "2":
        pelaaja = lataa_peli()
        
        if pelaaja is not None: # None tarkoittaisi, ettei pelaaja-oliota saatu ladattua
            break # Eli jos pelaaja ei ole None niin sitten pois

# --- Toiminta funktioita --- #

def tyhjennä_ruutu(): 
    os.system("clear")

def aloita_peli():
    print(f'\nAloitetaan peli, onnea matkaan {pelaaja.nimi}!')

def pelin_ohjeet():
    with open("ohjeet.txt", "r") as tiedosto:
        print(tiedosto.read())

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
            pelaaja.kerää_esine(lapio)
            print("Lapio lisätty.")
        elif sisältö == "2":
            pelaaja.kerää_esine(lamppu)
            print("Lamppu lisätty.")
        elif sisältö == "3":
            pelaaja.kerää_esine(kirves)
            print("Kirves lisätty.")
        elif sisältö == "4":
            pelaaja.kerää_esine(jakoavain)
            print("Jakoavain lisätty")
        elif sisältö == "5":
            pelaaja.raha = 100
            print("100€ käteistä rahaa lisätty.")
        elif sisältö == "6":
            break
        else:
            print("\nValitse 1-6. Kokeillaan uudestaan.")

def näytä_reppu():
    if pelaaja.reppu == []:
        print('\nReppusi on vielä tyhjä')

    else:
        print('\n=== Reppusi sisältö ===\n')
        for tavara in pelaaja.reppu:
            print(tavara.nimi)

    print(f"\nRahaa: {pelaaja.raha} €")

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
    exit()

def pelin_arvostelu(arvosana):
    if arvosana >= 1 and arvosana <=5:
        return f"Annoit arvosanaksi: {arvosana}"
    else:
        return "Arvosanan tulee olla väliltä (1-5)"

# --- Huoneiden funktioita --- #

def huone_kaupunki():
    print("\n=== Kaupunki ===")
    print("\nOlet saapunut kaupunkiin...")
    print("Tämä on matkasi alkupiste ja tästä matkamme alkaa")
    print("Näet edessäsi kolme eri vaihtoehtoa:")
    print("\nKaunis vehertävä metsä")
    print("Hieman ränsistyneen näköinen kauppa")
    print("Ovi, joka on raollaan ja siitä näkee, että se on pyörävarasto")

    while True:
        print("\nMinkä haluaisit tehdä seuraavista vaihtoehdoista?")
        print("1. Aloita matkasi metsästä")
        print("2. Aloita matkasi kaupasta")
        print("3. Aloita matkasi pyörävarastosta")
        print("4. Tarkista vielä reppusi sisältö")
        print("5. Tallenna ja lopeta peli")
        print("6. Lopeta peli")

        valinta = input("\nValitse vaihtoehto (1-6):\n")

        if valinta == "1":
            print("\nAsia kunnossa, jatkamme matkaamme metsään")
            paina_enter()
            pelaaja.liiku(metsä)
            tyhjennä_ruutu()
            break

        elif valinta == "2":
            print("\nAsia kunnossa, jatkamme matkaamme kauppaan")
            paina_enter()
            pelaaja.liiku(kauppa)
            tyhjennä_ruutu()
            break

        elif valinta == "3":
            print("\nAsia kunnossa, jatkamme matkaamme pyörävarastoon")
            paina_enter()
            pelaaja.liiku(pyörävarasto)
            tyhjennä_ruutu()
            break

        elif valinta == "4":
            näytä_reppu()
            paina_enter()
            tyhjennä_ruutu()

        elif valinta == "5":
            paina_enter()
            tallenna_peli(pelaaja)
            lopeta_peli()
        
        elif valinta == "6":
            paina_enter()
            lopeta_peli()

        else:
            print("\nSe ei ollut vaihtoehto, valitse (1-6)")

def huone_metsä():
    print("\n=== Metsä ====")
    print("\nOlet saapunut vehreään metsään, jossa huokuu luonnon raikkaus")
    print("Aurinko värähtelee vasten ihoasi puiden läpi ja kuulet pienen joen liplattelemassa lähistöllä")
    print("Yhtäkkiä huomaat, että edessäsi on tie, mutta liikkumista estää tielle kaatunut puu")

    while True:
        print("Sinulla on 4 vaihtoehtoa:")
        print("\n1. Yritä raivata kaatunut puu pois tieltä")
        print("2. Tarkista reppusi sisältö")
        print("3. Palaa takaisin kaupunkiin")
        print("4. Tallenna ja lopeta peli")
        print("5. Lopeta peli")

        valinta = input("\nMinkä valitset vaihtoehdoksesi (1-5)?\n")

        if valinta == "1":
            if kirves in pelaaja.reppu:
                print("\nHienoa, sinulla on kirves mukanasi")
                print("Voimme kirveelläsi hakata puuta ja raivata tiemme läpi, jotta pääsemme jatkamaan")
                print("Muista, että suojellaksemme luontoa, tee vain tarvittavat katkaisut puuhun ja jätä nämä pölkyt lahoamaan maahan")
                print("Se on paras ratkaisu tässä tapauksessa, koska puu on pakko siirtää jos haluamme jatkaa matkaa")
                print("\nHyvä, puu on nyt oikealla tavalla katkaistu ja pääsemme matkamaan matkaamme joelle")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(joki)
                break

            else:
                print("\nVoi himputti, et ottanut kirvestä mukaan alussa")
                print("Se ei haittaa, koska saatoimme nähdä jotain kiiltävää luonnossa juuri hetki sitten kun kävelimme eteenpäin")
                print("\nTuolta kiven alta pilkottaa jotain, mene katsomaan mitä siellä on")
                print("\n1. Tutki kiven alla oleva esine")
                print("2. Jätä esine rauhaan")

                tutki_valinta = input("Valitse vaihtoehdoista (1-2):\n")

                if tutki_valinta == "1":
                    print("\nLöysit kiven alta todella vanhan kirveen, se voi auttaa sinua tässä tehtävässä")
                    print("Haluatko ottaa kirveen talteen?")
                    print("\n1. Kyllä")
                    print("2. En")

                    ala_valinta = input("Valitse (1-2):\n")

                    if ala_valinta == "1":
                        print("\nMahtavaa, lisätään kirves talteen.")
                        pelaaja.kerää_esine(kirves)
                        print("Voimme kirveelläsi hakata puuta ja raivata tiemme läpi, jotta pääsemme jatkamaan")
                        print("Muista, että suojellaksemme luontoa, tee vain tarvittavat katkaisut puuhun ja jätä nämä pölkyt lahoamaan maahan")
                        print("Se on paras ratkaisu tässä tapauksessa, koska puu on pakko siirtää jos haluamme jatkaa matkaa")
                        print("\nHyvä, puu on nyt oikealla tavalla katkaistu ja pääsemme matkamaan matkaamme joelle")
                        paina_enter()
                        tyhjennä_ruutu()
                        pelaaja.liiku(joki)
                        break

                    elif ala_valinta == "2":
                        print("\nEt voi jatkaa matkaasi metsässä, käännytään ympäri takaisin kaupunkiin")
                        pelaaja.liiku(kaupunki)
                        break

                    else:
                        print("Väärä valinta, valitse (1-2)")

                elif tutki_valinta == "2":
                    print("\nAsia kunnossa, jätetään esine rauhaan")
                    print("Valitettavasti emme voi jatkaa matkaamme metsässä ilman kirvestä")
                    print("Palaamme kaupunkiin")
                    pelaaja.liiku(kaupunki)
                    break

                else:
                    print("\nSe ei ollut vaihtoehto, valitse (1-2)")

        elif valinta == "2":
            näytä_reppu()
            paina_enter()
            tyhjennä_ruutu()
            

        elif valinta == "3":
            print("\nAsia kunnossa, siirrytään takaisin kaupunkiin")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(kaupunki)
            break

        elif valinta == "4":
            paina_enter()
            tallenna_peli(pelaaja)
            lopeta_peli()

        elif valinta == "5":
            paina_enter()
            lopeta_peli()

        else:
            print("\nSe ei ollut vaihtoehtona, valitse (1-5)")
    
def huone_joki():
    print("\n=== Joki ====")
    print("\nOlet saapunut joelle, jossa vesi liplattaa ja tunnet luonnon läheisyyden")
    print(f"Selvisit äsköisestä haasteesta, hyvä {pelaaja.nimi}!")
    print("Joet ovat elintärkeitä sekä ihmiskunnalle, mutta oikeastaan enemmän vielä luonnon antimille")
    print("Joet tarjoavat kodin kasveille, kaloille, hyönteisille ja muille eläimille")
    print("Koska joki on tärkeä asia koko ihmiskunnalle, meidän pitäisi suojella sitä")
    print("Huomaat joessa roskia, pitäisikö sinun kerätä ne?")

    while True:
        print("\nSinulla on 5 vaihtoehtoa:")
        print("\n1. Kerää roskat")
        print("2. Älä kerää roskia")
        print("3. Tarkista reppusi sisältö")
        print("4. Palaa takaisin metsään")
        print("5. Tallenna ja lopeta peli")
        print("6. Lopeta peli")

        valinta = input("\nValitse (1-6):\n")

        if valinta == "1":
            print("\nSe oli oikea päätös, roskat ovat nyt kerätty ja pääset jatkamaan matkaa.")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(leiripaikka)
            break

        elif valinta == "2":
            print("\nJos et kerää roskia, en voi päästää sinua jatkamaan matkaasi")
            print("Roskien kerääminen auttaa suojelemaan luontoa sekä vettä, joka on kestävän kehityksen teema")
            print("Annan sinulle vielä 2 vaihtoehtoa")
            print("\n1. Kerää roskat")
            print("2. Älä kerää roskia")

            roska_valinta = input("\nValitse (1-2):\n")

            if roska_valinta == "1":
                print("\nHyvä, roskat ovat nyt kerätty ja voit jatkaa matkaasi")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(leiripaikka)
                break

            elif roska_valinta == "2":
                print("\nEn voi antaa sinun jatkaa matkaasi, koska et suostu suojelemaan luontoa")
                print("Palaat takaisin kaupunkiin ja aloitat matkasi alusta")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(kaupunki)
                break

            else:
                print("\nSe ei ollut vaihtoehto")
                paina_enter()
                tyhjennä_ruutu()

        elif valinta == "3":
            näytä_reppu()
            paina_enter()
            tyhjennä_ruutu()

        elif valinta == "4":
            print("\nPalataan takaisin metsään")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(metsä)
            break

        elif valinta == "5":
            paina_enter()
            tallenna_peli(pelaaja)
            lopeta_peli()
        
        elif valinta == "6":
            paina_enter()
            lopeta_peli()

        else:
            print("\nSe ei ollut vaihtoehtona, yritä uudelleen")
            paina_enter()
            tyhjennä_ruutu()

def huone_leiripaikka():
    print("\n=== Leiripaikka ====")
    print(f"\nHienoa, olen ylpeä sinusta {pelaaja.nimi}, keräsit roskat ja suojelit luontoa")
    print("Olet saapunut leirintäalueelle, et oikeastaan nää mitään, koska on niin pimeää")
    print("Olikohan sinulla lamppu mukana?")

    while True:

        if lamppu in pelaaja.reppu:
            print("\nMahtava homma, olet pakannut lampun mukaan matkalle")
            print("Huomaat taas leirintäpaikalla useita roskia, ketkäköhän on ne jättänyt sinne...")
            print("Haluatko kerätä roskat mukaan?")
            print("\n1. Kyllä")
            print("2. En")
            print("3. Tallenna ja lopeta peli")

            valinta = input("\nValitse (1-3):\n")

            if valinta == "1":
                print("\nSe oli oikea vaihtoehto, kerätään roskat ja jatkamme matkaa")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(tukikohta)
                break

            elif valinta == "2":
                print("\nEn voi antaa sinun jatkaa matkaasi, jos et suostu suojelemaan luontoa")
                print("Palaamme siis takaisin kaupunkiin ja saat aloittaa matkasi alusta")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(kaupunki)
                break

            elif valinta == "3":
                paina_enter()
                tallenna_peli(pelaaja)
                lopeta_peli()

        else:
            print("\nSinulla ei ole lamppua matkassasi")
            print("Astut jonkun kovan asian päälle, mutta se ei vaikuta kiveltä")

            if lapio in pelaaja.reppu:
                print("\nHyvä, että sinulla on lapio mukanasi, koita kaivaa")
                print("Löysit sieltä maan alta sodan aikaisen lampun!")
                print("Nyt näät ympärillesi ja huomaat leiri paikan olevan sotkua täynnä ja roskia")
                print("Haluatko kerätä roskat?")
                print("\n1. Kyllä")
                print("2. En")
                print("3. Tallenna ja lopeta peli")

                ala_valinta = input("\nValitse vaihtoehdoista (1-3):")

                if ala_valinta == "1":
                    print("\nHienoa, haluat taas suojella luontoa, keräämme siis roskat ja jatkamme matkaa")
                    paina_enter()
                    tyhjennä_ruutu()
                    pelaaja.liiku(tukikohta)
                    break

                elif ala_valinta == "2":
                    print("\nEn voi sinun antaa jatkaa matkaasi, jos et halua suojella luontoa")
                    print("Palaamme takaisin kaupunkiin ja aloitat matkasi alusta")
                    paina_enter()
                    tyhjennä_ruutu()
                    pelaaja.liiku(kaupunki)
                    break
            
                elif ala_valinta == "3":
                    paina_enter()
                    tallenna_peli(pelaaja)
                    lopeta_peli()

                else:
                    print("\nSe ei ollut vaihtoehtona, kokeile uudelleen")
                    paina_enter()
                    tyhjennä_ruutu()

            else:
                print("\nKoita kaivaa käsillä, jotain siellä on...")
                print("Wau, löysit sodan aikaisen lampun")
                print("Voit käyttää sitä valaisemaan ympäristöäsi, huomaat samalla, että leirintäpaikka on täynnä roskia")
                print("Haluatko kerätä roskat mukaan?")
                print("\n1. Kyllä")
                print("2. En")
                print("3. Tallenna ja lopeta peli")

                ala_valinta = input("\nValitse vaihtoehdoista (1-3):")
                
                if ala_valinta == "1":
                    print("\nHienoa, haluat taas suojella luontoa, keräämme siis roskat ja jatkamme matkaa")
                    paina_enter()
                    tyhjennä_ruutu()
                    pelaaja.liiku(tukikohta)
                    break
                
                elif ala_valinta == "2":
                    print("\nEn voi sinun antaa jatkaa matkaasi, jos et halua suojella luontoa")
                    print("Palaamme takaisin kaupunkiin ja aloitat matkasi alusta")
                    paina_enter()
                    tyhjennä_ruutu()
                    pelaaja.liiku(kaupunki)
                    break

                elif ala_valinta == "3":
                    paina_enter()
                    tallenna_peli(pelaaja)
                    lopeta_peli()
                
                else:
                    print("\nSe ei ollut vaihtoehtona, kokeile uudelleen")
                    paina_enter()
                    tyhjennä_ruutu()

def huone_kauppa():
    print("\n=== Kauppa ====")
    print("\nTervetuloa kauppaan, tämä on matkasi ensimmäinen kunnon pysäkki")
    print("Huomaat, että kauppias on heittämässä täysin käyttökelpoista tavaraa roskiin")
    print("Sinulla on seuraavat vaihtoehdot:")

    while True:

        print("\n1. Ehdota tavaroiden lahjoittamista / kierrättämistä")
        print("2. Anna kauppiaan vaan heittää tavarat pois ilman sinun puuttumista asiaan")
        print("3. Tutki kauppaa")
        print("4. Tarkista reppusi sisältö")
        print("5. Palaa takaisin kaupunkiin")
        print("6. Tallenna ja lopeta peli")
        print("7. Lopeta peli")
        
        valinta = input("\nAnna valintasi (1-7):\n")

        if valinta == "1":
            print("\nSe oli hyvä valinta, nyt kauppias päättää lahjoittaa tavarat hyväntekeväisyyteen")
            print("Käyttökelpoista tavaraa ei ikinä pidä heittää pois turhaan")
            print("Pääset jatkamaan matkaasi")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(metroasema)
            break

        elif valinta == "2":
            print("\nTavaroiden pois heittäminen olisi aivan turhaa tuhlaamista")
            print("Sinulla on vielä uusi mahdollisuu valita, että annatko hänen heittää tavarat pois vai kehotatko häntä lahjoittamaan tavarat?")
            print("\n1. Annan heittää pois")
            print("2. Ehdotan, että hän lahjoittaisi tavarat")

            ala_valinta = input("\nValitse (1-2):\n")

            if ala_valinta == "1":
                print("\nTäysin väärä valinta, käyttökelpoisen tavaran pois heittäminen on turhaa ja huonoksi luonnolle")
                print("Siirryt nyt takaisin kaupunkiin")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(kaupunki)
                break

            elif ala_valinta == "2":
                print("\nSe oli oikea valinta, pääset jatkamaan matkaa")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(metroasema)
                break

        elif valinta == "3":
            print("\nPäätit tutkia kauppaa, hieno valinta")
            print("Löysit palvelupisteen, jossa myydään sekä käytettyä, että uutta tavaraa")
            print("Myyjä tarjoaa sinulle seuraavia vaihtoehtoja:")
            print("\n1. Uusi taskulamppu - 30 €")
            print("2. Käytetty, mutta täysin toimiva taskulamppu - 10 €")
            print("3. Älä osta kumpaakaan")

            kauppa_valinta = input("\nMinkä valitset (1-3):\n")

            if kauppa_valinta == "1":
                
                if pelaaja.raha >= 30:

                    if lamppu in pelaaja.reppu:
                        print("\nSinulla oli jo pakattuna täysin toimiva lamppu")
                        print("Uuden tavaran ostaminen ilman tarvetta kuluttaa turhaan luonnonvaroja")
                        print("Uutta lamppua ei lisätty reppuusi")
                        print("Palaat takaisin kauppaan")
                        paina_enter()
                        tyhjennä_ruutu()
                        pelaaja.liiku(kauppa)
                    
                    else:
                        print("\nOstit uuden lampun, mutta olisit myös voinut ostaa käytetyn lampun")
                        print("Kun ostat käytettyä tavaraa, niin säästät luonnon varoja")
                        print("Lisätään lamppu reppuusi")
                        pelaaja.kerää_esine(lamppu)
                        pelaaja.raha -= 30
                        print("Palataan takaisin kauppaan")
                        paina_enter()
                        tyhjennä_ruutu()
                        pelaaja.liiku(kauppa)
                
                else:
                    print("\nSinulla ei ole tarpeeksi rahaa, takaisin kauppaan")
                    paina_enter()
                    tyhjennä_ruutu()
                    pelaaja.liiku(kauppa)
                        
            elif kauppa_valinta == "2":
                
                if pelaaja.raha >= 10:
                    
                    if lamppu in pelaaja.reppu:
                        print("\nSinulla oli jo toimiva lamppu, näin ollen et tarvitse lamppua enään")
                        print("Hienoa, että valitsit kuitenkin käytetyn lampun, se on järkevämpää")
                        print("Tässä tilanteessa lamppua ei kuitenkaan lisätä reppuusi")
                        print("Palataan takaisin kauppaan")
                        paina_enter()
                        tyhjennä_ruutu()
                        pelaaja.liiku(kauppa)

                    else:
                        print("\nHienoa, ostit käytetyn lampun, tämä on järkevää luonnon resurssien säästämiseksi")
                        print("Jos olisit ostanut uuden lampun, olisi se ollut vähän turhaa tuhlaamista")
                        print("Lisätään lamppu reppuusi")
                        print("Siirrytään myös takaisin kauppaan")
                        pelaaja.raha -= 10
                        pelaaja.kerää_esine(lamppu)
                        paina_enter()
                        tyhjennä_ruutu()
                        pelaaja.liiku(kauppa)

                else:
                    print("\nSinulla ei ole tarpeeksi rahaa, takaisin kauppaan")
                    paina_enter()
                    tyhjennä_ruutu()
                    pelaaja.liiku(kauppa)

            elif kauppa_valinta == "3":
                print("\nOkei, palataan takaisin kauppaan")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(kauppa)
                
            else:
                print("\nSe ei ollut vaihtoehto, valitse (1-3)")
                
        elif valinta == "4":
            näytä_reppu()
            paina_enter()
            tyhjennä_ruutu()

        elif valinta == "5":
            print("\nSiirrytään kaupunkiin")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(kaupunki)
            break
        
        elif valinta == "6":
            paina_enter()
            tallenna_peli(pelaaja)
            lopeta_peli()

        elif valinta == "7":
            paina_enter()
            lopeta_peli()
        
        else:
            print("\nSe oli väärä valinta, valitse (1-7)")
            paina_enter()
            tyhjennä_ruutu()
    
def huone_metroasema():
    print("\n=== Metroasema ====")
    print("\nOlet saapunut metroasemalle, seuraava metro on lähtemässä pian")
    print("Huomaat heti sisääntullessa lippuautomaatin, mutta samalla huomaat että ihmiset menevät metroon myös ilman lippua")
    print("Tässä seuraavat vaihtoehdot:")
    
    while True:
        print("\n1. Osta metrolippu ennen metroon menoa - 3 €")
        print("2. Mene metroon ostamatta lippua")
        print("3. Tarkista rahatilanteesi")
        print("4. Palaa kaupunkiin")
        print("5. Tallenna ja lopeta peli")
        print("6. Lopeta peli")

        valinta = input("\nMinkä valitset (1-6):\n")

        if valinta == "1":
            if pelaaja.raha >= 3:
                print("\nOstit lipun ja voit jatkaa matkaa metroon")
                print("Metro on matkalla keskustaan...")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.raha -= 3
                pelaaja.liiku(keskusta)
                break
            
            else:
                print("\nSinulla ei ole tarpeeksi rahaa matkustaaksesi lipun kanssa")
                paina_enter()
                tyhjennä_ruutu()
            
        elif valinta == "2":
            print("\nOlet päättänyt matkustaa ilman lippua...")
            print("Nouset tyytyäisenä metroon ja ovet sulkeutuvat ja metro nytkähtää liikkeelle")
            print("Seuraavalla pysäkillä huomaat, että lipuntarkastaja nousee kyytiin...")
            print("\nLipuntarkastaja: 'Matkalippujen tarkistus' ")
            print("\nPieni paniikki iskee...")
            print("\nLipuntarkastaja kertoo, ettei julkisessa liikenteessä voi matkustaa ilman lippua")
            print("Sinulla ei ole lippua jolla matkustaa, joten sinut lähetetään takaisin kaupunkiin")
            print("Lipputuloilla esimerkiksi rahoitetaan julkistaliikennettä, joka on hyödyllinen luonnonvarojen säästämisessä")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(kaupunki)
            break
        
        elif valinta == "3":
            print(f"Sinulla on rahaa: {pelaaja.raha} €")
            paina_enter()
            tyhjennä_ruutu()
            
        elif valinta == "4":
            print("\nPalataan takaisin kaupunkiin")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(kaupunki)
            break
            
        elif valinta == "5":
            paina_enter()
            tallenna_peli(pelaaja)
            lopeta_peli()

        elif valinta == "6":
            paina_enter()
            lopeta_peli()
        
        else:
            print("\nSe ei ollut vaihtoehto, valitse (1-6)")
            paina_enter()
            tyhjennä_ruutu()

def huone_keskusta():
    print("\n=== Keskusta ====")
    print("\nOlet saapunut keskustaan ja huomaat, että kahvilan työntekijä on heittämässä syömäkelpoista ruokaa roskiin")
    print("Valitse seuraavista vaihtoehdoista:")
    
    while True:
        print("\n1. Ehdota ruoan lahjoittamista")
        print("2. Anna ruoan päätyä roskiin")
        print("3. Palaa kaupunkiin")
        print("4. Tallenna ja lopeta peli")
        print("5. Lopeta peli")

        valinta = input("\nMinkä valitset (1-5):\n")

        if valinta == "1":
            print("\nSe oli oikea vaihtoehto, ruoka päätyy näin oikeaan paikkaan ja säästämme siinäkin luontoa")
            print("Jatkamme matkaa eteenpäin...")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(tukikohta)
            break
            
        elif valinta == "2":
            print("\nHuono vaihtoehto, syömäkelpoinen ruoka pois heitettäessä lisää ruokahävikkiä")
            print("\nOletko varma päätöksestäsi?")
            print("\n1. Kyllä")
            print("2. Ehdota lahjoittamista")

            ala_valinta = input("\nValitse (1-2):\n")

            if ala_valinta == "1":
                print("\nVäärä valinta, palaamme takaisin kaupunkiin")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(kaupunki)
                break

            elif ala_valinta == "2":
                print("\nSe oli oikea valinta, ruoka päätyy näin sitä tarvitseville ja luontoa säästyy")
                print("Matkamme jatkuu...")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(tukikohta)
                break
            
            else:
                print("\nSe ei ollut vaihtoehto, valitse (1-2)")
                paina_enter()
                tyhjennä_ruutu()

        elif valinta == "3":
            print("\nSelvä, palaamme kaupunkiin")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(kaupunki)
            break

        elif valinta == "4":
            paina_enter()
            tallenna_peli(pelaaja)
            lopeta_peli()
        
        elif valinta == "5":
            paina_enter()
            lopeta_peli()
        
        else:
            print("\nSe ei ollut vaihtoehto, valitse (1-5)")
            paina_enter()
            tyhjennä_ruutu()
            
def huone_pyörävarasto():
    print("\n=== Pyörävarasto ====")
    print("\nTervetuloa kolkkoon pyörävarastoon")
    print("Katsot ympärillesi ja pyörävarasto on aika ahdas, mutta jotain mielenkiintoista näkyy oikealla...")
    print("Sinulla on seuraavat vaihtoehdot:")

    while True:
        print("\n1. Mene tutkimaan")
        print("2. Älä tutki, lähden takaisin kaupunkiin")
        print("3. Tarkista reppu")
        print("4. Tallenna ja lopeta peli")
        print("5. Lopeta peli")

        valinta = input("\nValitse vaihtoehdoista (1-5):\n")

        if valinta == "1":
            print("\nHyvä päätös, löysit varaston nurkasta vanhan polkupyörän")
            print("Polkupyörä ei kuitenkaan ole aivan ajokuntoinen vielä, ota se mukaan matkallesi")
            pelaaja.kerää_esine(polkupyörä)
            print("Siirrytään eteenpäin...")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(korjaamo)
            break

        elif valinta == "2":
            print("\nSelvä homma, takaisin kaupunkiin")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(kaupunki)
            break

        elif valinta == "3":
            näytä_reppu()
            paina_enter()
            tyhjennä_ruutu()

        elif valinta == "4":
            paina_enter()
            tallenna_peli(pelaaja)
            lopeta_peli()
        
        elif valinta == "5":
            paina_enter()
            lopeta_peli()

        else:
            print("\nSe ei ollut vaihtoehto, valitse (1-5)")
            paina_enter()
            tyhjennä_ruutu()

def huone_korjaamo():
    print("\n=== Korjaamo ====")
    print("\nTervetuloa korjaamolle, olet saapunut tänne sen rikkinäisen polkupyörän kanssa")
    print("Se on oikeastaan hyvä asia että päädyit tänne, koska täältä löytyy varmasti jotain jolla korjata pyörä")

    if jakoavain in pelaaja.reppu:
        print("\nLoistavaa! Sulla on itseasiassa jo jakoavain mukana, sillä voimme heti korjata pyörän ja lähteä liikkeelle")
        print("Vanhan pyörän korjaaminen antaa sille uuden käyttöiän sen sijaan, että se päätyisi jätteeksi")
        print("Pyörä on nyt korjattu ja pääset jatkamaan matkaa...")
        paina_enter()
        tyhjennä_ruutu()
        pelaaja.liiku(pyörätie)

    else:
        print("\nHmm, sulla ei ole jakoavainta mukana ilmeisesti, joten pitää etsiä")
        print("Tuolla edessä kiiltää jotain, mene katsomaan!")

        while True:
            print("\n1. Mene katsomaan")
            print("2. En mene katsomaan")
            print("3. Tallenna ja lopeta peli")
            print("4. Lopeta peli")

            valinta = input("\nValitse vaihtoehdoista (1-4):\n")

            if valinta == "1":
                print("\nLöysit jakoavaimen! Tällä voimme korjata pyöräsi")
                print("Ensiksi lisätään jakoavain reppuusi")
                pelaaja.kerää_esine(jakoavain)
                print("Pyörä on nyt korjattu, voit jatkaa matkaa")
                print("Vanhan pyörän korjaaminen antaa sille uuden käyttöiän sen sijaan, että se päätyisi jätteeksi")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(pyörätie)
                break

            elif valinta == "2":
                print("\nEt voi valitettavasti jatkaa matkaasi ilman pyörää, matka on niin pitkä")
                print("Lähetetään sinut takaisin kaupunkiin")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(kaupunki)
                break

            elif valinta == "3":
                paina_enter()
                tallenna_peli(pelaaja)
                lopeta_peli()
            
            elif valinta == "4":
                paina_enter()
                lopeta_peli()
            
            else:
                print("\nSe ei ollut vaihtoehtona, valitse (1-4)")
                paina_enter()
                tyhjennä_ruutu()

def huone_pyörätie():
    print("\n=== Pyörätie ====")
    print("\nEdessäsi on todella pitkä pyörätie, tukikohta häämöttää jo horisontissa")
    print("Annan sinulle muutaman vaihtoehdon...")

    while True:
        print("\n1. Jatka matkaa polkupyörällä")
        print("2. Jätä pyörä ja ota taksi")
        print("3. Tarkista reppu")
        print("4. Palaa kaupunkiin")
        print("5. Tallenna ja lopeta peli")
        print("6. Lopeta peli")

        valinta = input("\nValitse vaihtoehdoista (1-6):\n")

        if valinta == "1":
            print("\nTäysin oikea valinta")
            print("Pyörällä liikkuminen taksin sijaan on loistavaa kestävän kehityksen kannalta")
            print("Pyöräillään tukikohtaan...")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(tukikohta)
            break
        
        elif valinta == "2":
            print("\nSe ei ole hyvä vaihtoehto kestävän kehityksen kannalta, haluatko kokeilla uudelleen?")
            print("\n1. Kyllä")
            print("2. En")

            ala_valinta = input("\nValitse (1-2):\n")

            if ala_valinta == "1":
                print("\nHyvä, kokeile valita uudelleen")
                paina_enter()
                tyhjennä_ruutu()

            elif ala_valinta == "2":
                print("\nJoudut takaisin kaupunkiin, koska se ei ole hyvä kestävän kehityksen kannalta")
                paina_enter()
                tyhjennä_ruutu()
                pelaaja.liiku(kaupunki)
                break

            else:
                print("\nSe ei ollut vaihtoehto, kokeile (1-2)")
                paina_enter()
                tyhjennä_ruutu()

        elif valinta == "3":
            näytä_reppu()
            paina_enter()
            tyhjennä_ruutu()

        elif valinta == "4":
            print("\nPalataan takaisin kaupunkiin...")
            paina_enter()
            tyhjennä_ruutu()
            pelaaja.liiku(kaupunki)
            break

        elif valinta == "5":
            paina_enter()
            tallenna_peli(pelaaja)
            lopeta_peli()
        
        elif valinta == "6":
            paina_enter()
            lopeta_peli()
        
        else:
            print("\nSe ei ollut vaihtoehto, valitse (1-6)")
            paina_enter()
            tyhjennä_ruutu()

def huone_tukikohta():
    print("\n=== Tukikohta ====")
    print("\nWow, en voi melkein uskoa tätä...")
    print(f"\nOlet läpäissyt pelin {pelaaja.nimi}!!!")
    print("Olet selviytynyt matkasta hienosti ja samalla olet oppinut luonnon sekä luonnonvarojen suojelemisesta")
    print("Olen todella ylpeä sinusta!!!")
    print("\nMatkamme on ohi, peli päättyy tähän")
    print(f"Kiitos pelaamisesta {pelaaja.nimi}!")

    while True:
        try:
            arvosana = int(input("\nAnna pelille vielä arvosana, valitse (1-5):\n"))

            if arvosana >= 1 and arvosana <= 5:
                print(pelin_arvostelu(arvosana))
                paina_enter()
                lopeta_peli()
            
            else:
                print("\nAnna numero väliltä (1-5)")
        
        except ValueError:
            print("\nTapahtui virhe, koita uudelleen syöttää (1-5)")

# --- Pelin silmukka --- #

def peli():
    while True: # tässä määritetään, että kun sijainti on == kaupunki niin suoritetaan kaupunki funktio ja niin edespäin
        if pelaaja.sijainti == kaupunki:
            huone_kaupunki()
        elif pelaaja.sijainti == metsä:
            huone_metsä()
        elif pelaaja.sijainti == joki:
            huone_joki()
        elif pelaaja.sijainti == leiripaikka:
            huone_leiripaikka()
        elif pelaaja.sijainti == kauppa:
            huone_kauppa()
        elif pelaaja.sijainti == metroasema:
            huone_metroasema()
        elif pelaaja.sijainti == keskusta:
            huone_keskusta()
        elif pelaaja.sijainti == pyörävarasto:
            huone_pyörävarasto()
        elif pelaaja.sijainti == korjaamo:
            huone_korjaamo()
        elif pelaaja.sijainti == pyörätie:
            huone_pyörätie()
        elif pelaaja.sijainti == tukikohta:
            huone_tukikohta()

# --- Päävalikko --- #

print(f"\nTervetuloa pelaamaan peliä {pelaaja.nimi}! ")

while True:
    print("\n=== Päävalikko ===")
    print("1. Ohjeet")
    print("2. Lisää tavaroita reppuusi")
    print("3. Reppusi sisältö")
    print("4. Krediitit")
    print("5. Aloita peli")
    print("6. Lopeta")

    valinta = input("\nValitse vaihtoehto (1-6):\n")

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
        peli()        

    elif valinta == "6":
        paina_enter()
        lopeta_peli()

    else:
        print("\nVäärä valinta, se ei ollut vaihtoehtona.")
        paina_enter()
        tyhjennä_ruutu()