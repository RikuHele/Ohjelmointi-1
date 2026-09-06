import random

player_name = input("\nTervetuloa peliin. Kerro nimesi:\n")
player_age = int(input(f"\nHauska tavata {player_name}! Kuinka vanha olet?\n"))
# nyt pelaajan ikä ja nimi tallennetaan muuttujiin

# --- Päävalikko --- #

print(f"\nTervetuloa pelaamaan peliä {player_name}! ")

while True:
    if player_age < 12:
        print("\nPelin ikäraja on 12v, peli sammutetaan.")
        exit()
    else:
        print("\n=== Päävalikko ===")
        print("1. Ohjeet")
        print("2. Tulokset")
        print("3. Krediitit")
        print("4. Lopeta")

        valinta = input("\nValitse vaihtoehto (1-3):\n")

        if valinta == "1":
            print("\nTässä ohjeet")
            enter = input("\nPaina enter kun olet valmis.")
            if enter == "":
                continue
            
        # Lisää ohjeet vielä myöhemmin

        elif valinta == "2":
            print("\nEi vielä tuloksia saatavilla")
            enter = input("\nPaina enter kun olet valmis.")
            if enter == "":
                continue

        elif valinta == "3":
            print("\nPelin tekijä on 21-vuotias tieto- ja viestintätekniikan opiskelija Metropolia Ammattikorkeakoulusta")
            enter = input("\nPaina enter kun olet valmis.")
            if enter == "":
                continue

        elif valinta == "4":
            print("\nLopetetaan päävalikko")
            break

        else:
            print("\nVäärä valinta, se ei ollut vaihtoehtona.")