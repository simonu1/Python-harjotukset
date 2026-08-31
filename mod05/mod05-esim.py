'''
suorita = True
while suorita:
    print('tämä printtaantuu vain kerran')
    #suorita = False
print('suoritusloppuu')
'''
'''
luku = 1 #alkuehto
while luku<= 5: #ehto
    print(luku)
    luku = luku + 1

print('jatketaan ohjelmaa')'''

# muutetaan ohjelma 10stä (alaspäin)
"""luku = int(input('anna luku josta lasketaan alas: '))
while luku > 1: #ehto
    print(luku)
    luku -= 1
"""

'''salasana = input('anna salasana ("python"): ').strip()

while salasana != 'python':
    print('väärä salasana')
    salasana = input('väärä salasana, anna uudesaan: ')

print('tervetuloa sisään, koodi oli oikein')'''

'''komento = input('anna komento (lopeta): ')

while komento != 'lopeta':
if komento == "apua":
        break
    print('annoit komennon: ', komento)
    komento = input('anna uusi komento: ')
else:
    print('annoit komennon lopeta')

print('ohjelma jatkuu')'''

import random

'''kierros = 0 
heitot = 0 
while kierros < 1000:

    nop1 = nop2 = 0
    while (nop1 != 6 or nop2 != 6):
        nop1 = random.randint(1,6)
        nop2 = random.randint(1,6)
        print(nop1, nop2)
        heitot += 1
    kierros += 1
print('pelikertoja oli:', kierros)
print(f'tarvittiin {heitot:d} heittoa.')
print(f'jokaisella kierroksella oli keskimäärin {heitot/kierros} heittoa')'''
'''
eka = 1
while eka <=5:
    toka = 1 
    while toka <= 5:
            print(f"{eka} kertaa {toka} on {eka+toka:d}")'''

