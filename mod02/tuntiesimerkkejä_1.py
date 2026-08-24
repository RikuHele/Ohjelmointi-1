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