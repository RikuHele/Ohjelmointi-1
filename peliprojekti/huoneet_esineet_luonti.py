
from luokat.esine import Esine
from luokat.huone import Huone

# --- Esineiden luonti --- #

lapio = Esine("Lapio", 2.0)
lamppu = Esine("Lamppu", 0.8)
kirves = Esine("Kirves", 2.5)
jakoavain = Esine("Jakoavain", 0.3)
polkupyörä = Esine("Polkupyörä", 4.0)

# --- Huoneiden luonti --- #

kaupunki = Huone("Kaupunki")
metsä = Huone("Metsä", kirves)
joki = Huone("Joki")
leiripaikka = Huone("Leiripaikka", lamppu)
kauppa = Huone("Kauppa", lamppu)
metroasema = Huone("Metroasema")
keskusta = Huone("Keskusta")
pyörävarasto = Huone("Pyörävarasto", polkupyörä)
korjaamo = Huone("Korjaamo", jakoavain)
pyörätie = Huone("Pyörätie")
tukikohta = Huone("Tukikohta")