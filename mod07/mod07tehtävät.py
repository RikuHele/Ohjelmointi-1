import random
import math

# Tehtävä 1

def noppapeli():
    return random.randint(1,6)

while True:
    heitto = noppapeli()
    print(heitto)

    if heitto == 6:
        break

# Tehtävä 2

x = int(input('Anna nopan tahkojen yhteismäärä:\n'))

def noppapeli(x):
    return random.randint(1, x)

while True:
    heitto = noppapeli(x)
    print(heitto)

    if heitto == x:
        break

# Tehtävä 3

def bensiini(x):
    return (x*3.785)

while True:
    x = float(input('\nAnna bensiinin määrä nestegallonoina:\n'))

    if x < 0:
        print('Tulos ei voi olla negatiivinen, lopetetaan ohjelma.')
        break

    print(f'\nBensiinin määrä on nyt litroissa {bensiini(x):.2f}')

# Tehtävä 4

def lista(l1):
    return sum(l1) 

l1 = [2, 3, 4]
print(lista(l1))

# Tehtävä 5

def f(l1):
    list2 = []
    for luku in l1:
        if luku % 2 == 0:
            list2.append(luku)
    return list2

l1 = [2, 5, 7, 10, 14, 15, 18]
print(f'Lista, josta karsittu parittomat: {f(l1)}')
print(f'Lista, joka on alkuperäinen: {l1}')

# Tehtävä 6

def pizza(halkaisija, hinta):
    halkaisija_m = halkaisija / 100
    pinta_ala = math.pi*(halkaisija_m/2)**2
    pizza_hinta_per_euro = hinta / pinta_ala
    return pizza_hinta_per_euro


halkaisija1 = float(input('\nAnna ensimmäisen pizzan halkaisija senttimetreinä:\n'))
hinta1 = float(input('\nEnsimmäisen pizzan hinta:\n'))
pizza1 = pizza(halkaisija1, hinta1)

halkaisija2 = float(input('\nAnna toisen pizzan halkaisija senttimetreinä:\n'))
hinta2 = float(input('\nToisen pizzan hinta:\n'))
pizza2 = pizza(halkaisija2, hinta2)
   
if pizza1 < pizza2:
    print(f'\nEnsimmäinen pizza on {pizza1:.2f} €/m² ja se on halvempi.')
    print(f'Toinen pizza on {pizza2:.2f} €/m².')
        

elif pizza1 > pizza2:
    print(f'\nToinen pizza on {pizza2:.2f} €/m² ja se on halvempi.')
    print(f'Ensimmäinen pizza on {pizza1:.2f} €/m².')
        

else:
    print(f'Molemmat pizzat ovat täysin saman hintaisia eli {pizza1:.2f} €/m².')


