# Funktiot

# def f(x):
#     print('Moi')
#     print(x)
#     return 3

# f(4)
#nyt tulostuu vain moi 4

# print(f(4))
#jos laittaa print, niin tulee myös myös return komennon arvo eli moi 4 3

# def f(x, y):
#     print(x)
#     print(y)
#     print('Moi')
#     print(2*x + 3*y)

# print(f(3, 2))

#tulee myös none, koska return ei ole määritelty. Jos ei anna return arvoa tulee aina none

# x = [1, 2, 3]
# y = x.append(4)
# print(y)
# print(x)

#nyt x tulostaa koko listan eli 1, 2, 3 ja 4. Y on funktio ja append on osa funktiota, sen takia tulostuu myös none
#se on ikäänkuin return arvona tässä

# def f(x, y):
#     return x + y

# print(f(2, 3))
#nyt funktio palauttaa määriteltyjen funktion parametrien summan

# def terve(x):
#     fstr = f"Terve {x}!"
#     return fstr

# print(terve("John"))
#fstr käytettäessä voidaan esim tehdä lauseita.

# def f(x, y, nimi):
#     if nimi == "erotus":
#         return x - y

#     elif nimi == "summa":
#         return x + y

# print(f(2, 2, nimi = "erotus" ))
#nimi = merkitsee nyt lasketaanko kahden ensimmäisen muuttujan erotus vai summa

# def f(list1):
#     list2 = []
#     for luku in l1:
#         if luku % 2 == 0:
#             list2.append(luku)
#     return list2

# l1 = [2, 5, 7, 10, 14, 18]
# print(f(l1))

#funktio, jolla l1 otetaan parilliset luvut ja laitetaan l2 listaan, eli uuteen listaan.

# def nimeni(nimi, kerta):
#     for n in range (kerta):
#         print (f"{nimi} {n + 1}.kerta")


# print(nimeni('James', 7))
#tässä funktio, johon laitetaan 'nimi' ja sitten numero joka kertoo kuinka monta kertaa nimi printataan.
#myös f'' saadaan esim. ensimmäinen, toinen tms.