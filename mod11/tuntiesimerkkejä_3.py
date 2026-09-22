# class Viesti:
#     lähetetty = 0
    
#     def __init__(self, sisältö):
#         self.sisältö = sisältö
#         Viesti.lähetetty += 1
#         # jos halutaan tietää montako viestiä on lähetetty, niin laitetaan viesti.lähetetty...
#         # määritellään myös luokan alussa yleinen lähetetty = 0
#         # voi myös laittaa Viesti.lähetetty = Viesti.lähetetty + 1
        

# viesti1 = Viesti('Ostitko maitoa?')
# viesti2 = Viesti('En')
# viesti3 = Viesti('Miksi?')

# print(f'Viestejä lähetetty: {Viesti.lähetetty} kpl')
# # print(Viesti.lähetetty) / tulostaa lähetettyjen viestien lukumäärän

# class Animal:
#     def __init__(self, paino):
#         self.paino = paino

#     def kävelee(self):
#         print('Minä olen eläin')

# class Dog(Animal):
#     def __init__(self, paino, häntä):
#         super().__init__(paino)
#         self.häntä = häntä
#     def kävelee(self):
#         super().kävelee()
#         print('Itse asiassa olen koira, joten kävelen nätisti')

# d1 = Dog(20, 'pitkä')
# d1.kävelee()

# # tässä harjoitellaan miten otetaan toisesta luokasta tietoja toiseen
# # super() tarkoittaa ylemmästä luokasta
# # tässä tapauksessa Dog(Animal), eli Animal on yläluokka ja Dog alaluokka

# class Muoto:
#     def __init__(self, väri):
#         self.väri = väri

#     def mittaa(self):
#         print('Nyt lasken piirin...')

# class Suorakulmio(Muoto):
#     def __init__(self, väri, pituus, leveys):
#         super().__init__(väri)
#         self.pituus = pituus
#         self.leveys = leveys
        
#     def mittaa(self):
#         super().mittaa()
#         print(f'Piiri on: {self.pituus + self.pituus + self.leveys + self.leveys}')


# s1 = Suorakulmio('Punainen', 3, 4)
# s1.mittaa()

# while True:
#     try:
#         luku = int(input('\nAnna joku luku: '))

#     except ValueError:
#         print("\nSe ei ollut luku! Kokeile uudelleen")
#         continue
    
#     print('\nJippii, ohjelma loppuu')
#     break

# # except ValueError: / tarkoittaa, että jos käyttäjä syöttää kirjaimia, niin tulee tuo printti. Ohjelma ei kaadu
# # vaan silloin se on ns. huomioitu ja ohjelma jatkuu vaikka syöttäjä laittaa väärän formaatin

# class Biisi:
#     def __init__(self, laulaja, biisin_nimi):
#         self.laulaja = laulaja
#         self.biisin_nimi = biisin_nimi

# b1 = Biisi('Los Palmeras', 'Cola')
# b2 = Biisi('Dave', 'Raindance')
# b3 = Biisi('Dave', 'Hangman')
# b4 = Biisi('Bad Bunny', 'DtMF')
# b5 = Biisi('Frank Sinatra', 'My Way')
# b6 = Biisi('The Outfield', 'Your Love')


# class Playlist:
#     def __init__(self):
#         self.munlista = []

#     def lisää_listaan(self, biisi):
#         self.munlista.append(biisi)
  

# lista = [b1, b2, b3]
# for b in lista:
#     print(f'{b.laulaja} - {b.biisin_nimi}')

# p1 = Playlist()
# p1.lisää_listaan(b1)
# for b in p1.munlista:
#     print(f'{b.laulaja} - {b.biisin_nimi}')

# # tässä ohjelma jossa on biisejä ja toinen luokka playlist jolla luodaan soittolistoja