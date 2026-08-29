# Tehtävä 1

kalan_koko = float(input("Kerro kalan pituus senttimetreinä:\n"))
alamitta = 37 - kalan_koko

if kalan_koko < 37:
    print(f"\nKalasi koko oli {kalan_koko}cm ja se on {alamitta}cm verran alamitasta. Se pitää laskea takaisin järveen.")
else:
    print(f"\nKalasi koko oli {kalan_koko} ja se on sopivan mittainen nostettavaksi.")

# Tehtävä 2

hyttiluokka = input("\nMikä hyttiluokka? LUX, A, B vai C?\n")

if hyttiluokka == "LUX":
    print("\nLUX on parvekkeellinen hytti yläkannella.")
elif hyttiluokka == "A":
    print("\nA on ikkunallinen hytti autokannen yläpuolella.")
elif hyttiluokka == "B":
    print("\nB on ikkunaton hytti autokannen yläpuolella.")
elif hyttiluokka == "C":
    print("\nC on ikkunaton hytti autokannen alapuolella.")
else:
    print("\nVirheellinen hyttiluokka.")

# Tehtävä 3

sukupuoli = input("\nIlmoita biologinen sukupuolesi:\n")
hemoglobiini = int(input("\nIlmoita hemoglobiiniarvosi: \n"))

if sukupuoli == "Nainen" or sukupuoli == "nainen":
    if 117 <= hemoglobiini <= 175:
        print(f"\nOlet {sukupuoli} ja hemoglobiiniarvosi on silloin normaali.")
    elif hemoglobiini > 175:
        print(f"\nOlet {sukupuoli} ja hemoglobiiniarvosi on silloin liian korkea.")
    elif hemoglobiini < 117:
        print(f"\nOlet {sukupuoli} ja hemoglobiiniarvosi on silloin liian matala.")

if sukupuoli == "Mies" or sukupuoli == "mies":
    if 134 <= hemoglobiini <= 195:
        print(f"\nOlet {sukupuoli} ja hemoglobiiniarvosi on silloin normaali.")
    elif hemoglobiini > 195:
        print(f"\nOlet {sukupuoli} ja hemoglobiiniarvosi on silloin liian korkea.")
    elif hemoglobiini < 134:
        print(f"\nOlet {sukupuoli} ja hemoglobiiniarvosi on silloin liian matala.")

# Tehtävä 4

vuosi = int(input("\nIlmoita vuosiluku niin kerron onko se karkausvuosi:\n"))

if vuosi % 400 == 0:
    print(f"\nVuotesi oli {vuosi} ja se on karkausvuosi.")
elif vuosi % 100 == 0:
    print(f"\nVuotesi oli {vuosi} ja se ei ole karkausvuosi.")
elif vuosi % 4 == 0:
    print(f"\nVuotesi oli {vuosi} ja se on karkausvuosi.")
else:
    print(f"\nVuotesi oli {vuosi} ja se ei ole karkausvuosi.")