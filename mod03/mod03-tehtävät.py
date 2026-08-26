import math

# a = float(input("anna ensimmäinen luku:\n"))
# b = float(input("anna toinen luku:\n"))

# yhteenlasku = a + b
# vähennyslasku = a - b
# kertolasku = a * b
# jakolasku = a / b
# potenssilasku = a ** b 
# kokonaisosa = a // b
# jakojaannos = a % b

# print(f'yhteenlasku: {yhteenlasku}')
# print(f'vähennyslasku: {vähennyslasku}')
# print(f'kertolasku: {kertolasku}')
# print(f'jakolasku: {jakolasku}')
# print(f'potenssilasku: {potenssilasku}')
# print(f'kokonaisosa: {kokonaisosa}')
# print(f'jakojäännös: {jakojaannos}')

#1

# print("no morjest")
# nimi = input("anna nimesi: ")
# print(f'terve, {nimi})

#2

#radius = float(input("anna säde: "))
#sade = (radius * radius) * math.pi
#print(f"ympyrän pinta-ala: {sade:.2f}")

#3

#sk = float(input("anna suorakulmion kanta: "))
#sp = float(input("anna suorakulmion korkeus: "))

#piiri = (sk * 2) + (sp * 2)
#pintaala = sk * sp

#print(f'suorakulmion piiri: {piiri} ja suorakulmion pinta-ala: {pintaala}')

#4

#a = float(input("anna ensimmäinen luku: "))
#b = float(input("anna toinen luku: "))
#c = float(input("anna kolmas luku: "))

#summa = a + b + c
#tulo = a * b * c
#keskiarvo = (a + b + c) / 3

#print(f'kolmen luvun summa: {summa}, tulo: {tulo}, ja keskiarvo {keskiarvo}')

#5

a = float(input("anna leiviskät: "))
b = float(input("anna naulat: "))
c = float(input("anna luodit: "))

leiviska_g = a * 20 * 32 * 13.3
naulat_g = b * 32 * 13.3
luodit_g = c * 13.3
yhteismassa = leiviska_g + naulat_g + luodit_g
kg = int(yhteismassa // 1000)
g = yhteismassa % 1000

print(f'Massa nykymittojen mukaan:')
print(f'{kg} kilogrammaa ja {g:.2f} grammaa.')

#6

#import random

#luku = random.randint(0, 9)
#luku2 = random.randint(0, 9)
#luku3 = random.randint(0, 9)
#print(f'{luku} {luku2} {luku3}')