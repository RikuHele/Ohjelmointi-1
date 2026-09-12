# Tehtävä 1

vuodenajat = ("talvi", "kevät", "kesä", "syksy")

kuukausi = int(input("Anna kuukauden numero (1-12):\n"))

if kuukausi in (12, 1, 2):
    print(f"\nAntamasi numero oli {kuukausi}, ja sen vuodenaika on {vuodenajat[0]}.")

elif kuukausi in (3, 4, 5):
    print(f"\nAntamasi numero oli {kuukausi}, ja sen vuodenaika on {vuodenajat[1]}.")

elif kuukausi in (6, 7, 8):
    print(f"\nAntamasi numero oli {kuukausi}, ja sen vuodenaika on {vuodenajat[2]}.")

elif kuukausi in (9, 10, 11):
    print(f"\nAntamasi numero oli {kuukausi}, ja sen vuodenaika on {vuodenajat[3]}.")

else:
    print("\nAntamasi kuukauden numero oli virheellinen.")

# Tehtävä 2

nimet = set()

while True:
    nimi = input("\nAnna nimi:\n")

    if nimi == "":
        break

    if nimi in nimet:
        print("Aiemmin syötetty nimi")

    else:
        nimet.add(nimi)
        print("Uusi nimi")

for n in nimet:
    print(n)

# Tehtävä 3

lentoasemat = {}

while True:
    print("\n1. Syötä uusi lentoasema")
    print("2. Hae lentoasema")
    print("3. Lopeta")

    valinta = input("\nAnna valintasi (1-3):\n")

    if valinta == "1":
        icao = input("\nAnna lentoaseman ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi

    elif valinta == "2":
        haettava_icao = input("\nAnna lentoaseman ICAO-koodi: ")

        if haettava_icao in lentoasemat:
            print(f'Antamasi lentoaseman nimi on: {lentoasemat[haettava_icao]}')

        else:
            print('Antamasi lentoasemaa ei ollut vielä tallennettu')

    elif valinta == "3":
        break

    else:
        print("\nAntamasi numero ei vastannut vaihtoehtoja")