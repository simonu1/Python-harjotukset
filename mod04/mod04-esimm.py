#sähkölaskunlaskin

kulutus = float(input("syötä sähkönkulutus (kWh):"))

if kulutus <= 50:
    #hinta aina 10 senttiä
    hinta = kulutus * 50 

elif kulutus <= 200:
    #ensimmäiset 50kWh 10 senttiä, seuraavat 150 kWh 8 senttiä
    hinta = 50 * 10
    hinta += (kulutus-50) * 8

else:
    #loput yli 200 kWh 6 senttiä/kWh
    hinta = 50 * 10
    hinta += 150 * 8
    hinta = hinta + (kulutus - 200) * 6

print(f'sähkön hinta {hinta//100:.0f},{hinta%100:.0f} euroa')