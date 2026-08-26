#print("Hello\nMitä kuuluu?")
# \n = rivivaihto, \t = tab eli 4 välilyöntiä
# \ = shift + option + 7

#print('Kalle sanoi: "Mitä kuuluu?"')
# print toimii sekä '≈', että "≈", jos esimerkiksi tarvitsee lainata sitaattia niin print('kalle sanoi: "mitä kuuluu"')


#print("Nimeni on Riku 😀")
# control + command + space = emojihaku
# tai esimerkiksi unicode.org ja sieltä esim. print("\U0001f600")
# tai esimerkiksi print("\N{grinning face}"), \N tarkoittaa = Name

#nimi = input("Kerro minulle nimesi: \n")
#print("Hei !" + nimi)
# input tarkoittaa, että käyttäjä voi esim. kirjoittaa oman nimesi tms 
# nimi = tarkoittaa että käyttää nimi tunnistetta koko ohjelman ajan ja tallentaa sen
# \n tekee nimen kirjoittamisen toiselle riville
# print("Hei !" + nimi) taas tarkoittaa että ohjelma moikkaa sinua takaisin omalla nimelläsi

#nimi = "james"
#lukupi = 3.141596
#sade = 4
#uusiluku = 3.0
#luku1 = 2
#luku2 = '2'
#luku3 = "2"
#booli = True
# sade = säde

#print("Ympyrän piiri on ")
#print(2*lukupi*sade)
# ympyrän ympärysmittä

#print("")
# tyhjä print(""), jotta tulosteesta tulee vähän käyttäjäystävällisempi

#print("Ympyrän pinta-ala on ")
#print(sade*sade*lukupi)
# ympyrän pinta-ala

#print(id(lukupi))
# id kertoo mihin muistipaikkaan lukupi on tallennettu

#import math
# tuo lisäominaisuuksia esim. matematiikan tehtäviin

#print(math.pi)
# esimerkiksi nyt printtaa pi:n numeron. pitää aina olla print(math.,,,) ,,, = jotain matikkaan liittyvää

#print(type(sade))
# int = kokonaisluku, ylempänä on sade =

#print(type(lukupi))
# float = desimaaliluku, ylempänä on lukupi = 

#print(type(uusiluku))
# float = desimaaliluku, ylempänä on uusiluku = 

#print(type(nimi))
# str = string eli merkkijono, ylempänä on nimi = 

#print(type(luku1))
#print(type(luku2))
#print(type(luku3))
#print(type(booli))
# ei toimi kun ei ole luku1 ei ole kokonaisluku int, luku2 on merkkijono str, luku3 on merkkijono str

#print(luku1 + luku1)
# toimii normaalisti eli 2 + 2

#print(luku2 + luku2)
# ei toimi normaalisti, koska kyseessä on str niin se vain liittää numerot 2 + 2 = 22

# + on plus, - on miinus, * on kertolasku, / on jakolasku ja ** on potenssi

#print(type(luku2 + luku2))
# = str, eli voi yhdistää

#print(luku2 * 4)
# = liittää jälleen numerot eli 4 * 2 = 2222 niinkuin rivillä 72


#print("Nimeni on Riku")
#sydän = "♥️"
#print("Haluan 50 sydäntä")
#print(50*sydän)
#print("Sukunimeni on Helenius")

#print(id(luku1))
# muistipaikan selvitys id: jos tarvii jostain syystä

#mu1 = 3
# integer

#mu2 = 3.5
# float

#mu3 = '3'
#string

#mu4 = True
#bool

#mu31 = int(mu3)
# muuttaa mu3 string -> integer

#print(mu31*2)
# testi, miltä nyt mu31 näyttää. mu3 on muuttunut string - > integer

#a, b = 3, 6
# pythonissa voi laittaa muuttujat samalle riville, jos erottelee ,:lla

#print(2 = 2)
# ei toimi, koska = tarkoittaa käskyä, esim a = 2

#print(2 == 2)
# toimii, koska == tarkoittaa kysymystä tai yhtäsuuri kuin
# != tarkoittaa, ei yhtäsuuri kuin

#luku1 = 100
#luku2 = 523

#print(f"{math.log10(luku1):.2f}")
#print(f"{math.log10(luku2):.2f}")

#print(luku2 / luku1)
#print(luku2 // luku1)

# / = jakolasku, float // = jakolasku, integer

#print(f'10 neliöjuuri on ≈ {math.sqrt(luku2):0.2f}')
# jos laittaa f ennen ' tai " niin kyseisen printin sisään voi tehdä aaltosulkujen sisään joko esim. matematiikan laskuja tai funktioita
# jos haluaa kokeilla pitää laittaa import math päälle

#luku = int(input("Anna minulle joku luku:\n"))

#print(f"\nAntamasi luku oli: {luku} ja\n")
# toimii myös mutta voi lisätä suoraan if lausekkeisiin

#if luku < 100:
    #print(f"Lukusi oli {luku} ja on pienempi kuin 100")
#elif luku == 100:
    #print(f"Lukusi oli {luku} ja on tasan 100")
#else:
    #print(f"Lukusi oli {luku} ja on yli 100")


#luku = int(input("Montako kertaa?:\n"))
#str1 = "Terve"

#print(f"{str1} {luku} kertaa!")

# luku = 28923

# if luku % 2 == 0:
#     print(f"Lukusi {luku} on parillinen")

# else:
#     print(f"Lukusi {luku} on pariton")