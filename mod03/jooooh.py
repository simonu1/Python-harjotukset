import math

teksti = "before i go broke like joc"

luku = input("anna 1. luku: ")
luku2 = input("anna 2. luku: ")

luku = float(luku) # esim "10.5" -> 10.5
luku2 =float(luku2)

summa = luku + luku2
print(f"lukujen {luku} ja {luku2} summa on {summa}")

#sama liitosoperaattorilla (+)
summa = str(summa)
print("summa:  " + summa)

print("lukujen " + str(luku) + " ja " + str(luku2) + " summa on " + summa + ".")

uusi_käyttäjä = input("anna nimesi")
ikä = input("anna ikäsi")
print("wazzzaaa, "+ uusi_käyttäjä)
print(f"wazzaaa {uusi_käyttäjä} ja olen {ikä}")

pisteet = 200
pisteet = 400
print(pisteet)

merkkijono = "jouko"

print(f'merkkijono: {merkkijono:<20s} sijoitetaan väliin')

kokonaisluku = -9
kokonaisluku_pitkä = 12_456_123_180
liukuluku = 4.973
kompleksiluku = -4 + 2j
totuusarvo = False

print(kompleksiluku)
print(kompleksiluku. real)
print( kompleksiluku. imag)

tyyppi  = type(totuusarvo)

print(f'muuttujan tyyppi voidaan tutkia {type(kompleksiluku)}')

print(f'{"vakio":12s}{"arvo" :12s}')
print("-------------")
print(f"{'Pii':12s}:{math.pi:10.4f}")

#tuloste1 = 
''' Laskutoimituksia ovat yhteenlasku (+),
vähennyslasku (-), 
 kertolasku (*)
 ja jakolasku (/).
 Lisäksi on olemassa jakojäännösoperaatio (%),
pelkän kokonaisosan palauttava jakolasku (//)
potenssiinkorotus (**).
'''


a = float(input("anna ensimmäinen luku:\n"))
b = float(input("anna toinen luku:\n"))

yhteenlasku = a + b
vähennyslasku = a - b
kertolasku = a * b
jakolasku = a / b
potenssilasku = a ** b 
kokonaisosa = a // b
jakojaannos = a % b

print(f'yhteenlasku: {yhteenlasku}')
print(f'vähennyslasku: {vähennyslasku}')
print(f'kertolasku: {kertolasku}')
print(f'jakolasku: {jakolasku}')
print(f'potenssilasku: {potenssilasku}')
print(f'kokonaisosa: {kokonaisosa}')
print(f'jakojäännös: {jakojaannos}')