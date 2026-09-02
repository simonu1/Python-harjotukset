#1
'''luku = 1
while luku <= 1000:
    #jos luku on 3 jaollinen, niin printtaa
    if luku % 3 == 0:
        print(luku)
    luku += 1
'''
#2

'''while True:
    inch = float(input('anna tuumat: '))
    
    if inch < 0:
        print('ohjelma loptetetaan')
        break
    
    cm = inch * 2.54
    print(f'{inch} tuumaa on {cm:.2f} senttimetriä\n')'''
#3

'''luvut = []

while True:
    syote = input('anna luku(tyhjä merkkijono lopettaa): ')
    if syote == "":
        break

    luku = float(syote)
    luvut.append(luku)

if luvut:
    print(f'\nPienin luku: {min(luvut)}')
    print(f'Suurin luku: {max(luvut)}')
else:
    print('\nEt syöttänyt yhtään lukua.')'''

#4
'''oikea_nro = 4
arv = int(input('arvaa 1-10 välillä: '))

while arv != oikea_nro: 
    print('väärin')
    arv = int(input("arvaa uudestaan: "))

print(f'oikea nro {oikea_nro}')'''

#5 
'''
kt = input("anna käyttäjätunnus (python): \n")
ss = input("anna salasana (rules): \n")

yritys = 1

while kt != 'python' or ss != 'rules':
    yritys += 1
    if yritys > 5:
        break
    kt = input("anna käyttäjätunnus (python): \n")
    ss = input("anna salasana (rules): \n")

if kt == 'python' and ss == 'rules':
    print('tervetuloa')
else:
    print('pääsy evätty')'''

#6
import random


N = int(input('anna arvottavien pisteiden määrä: '))

n = 0 # pisteet jotka osuivat ympyrän sisälle
i = 0 # montako pistettä on arvottu

while i < N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    print(f'{i}, arvotun pisteen koordinaatit x: {x:.2f}, y:{y:.2f}')
    i += 1
    if x**2 + y**2 < 1:
           n += 1
pii = 4 * n / N
print(f'Pi:n likiarvo: {pii}')
print(f'pisteitä arvottu yhteensä {N}, ympyrän sisälle osui {n} kpl')