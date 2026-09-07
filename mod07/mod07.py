#1

'''import random

def heita_noppaa():
    tulos = random.randint(1,6)
    return tulos

#pääohjelma
    #alustava muuttuja, ja tallennetaan viimeisin heitto
heiton_tulos = 0

#noppaa heitetään niin kauan kunnes tulee 6
while heiton_tulos != 6:
    heiton_tulos = heita_noppaa()
    print(f'heiton luku: {heiton_tulos}')
'''
#2


'''import random

def heita_noppaa(tahkot):
    tulos = random.randint(1,tahkot)
    return tulos

maksimi = int(input("anna nopan tahkojen määrä: "))

heiton_tulos = 0

#noppaa heitetään niin kauan kunnes tulee 6
while heiton_tulos != maksimi:
    heiton_tulos = heita_noppaa(maksimi)
    print(f'heiton luku: {heiton_tulos}')
'''

#3

'''def gallon_litra(gallonat):
    litrat = gallonat * 3.785
    return litrat


syote = float(input('anna bensan määrä gallonina: '))

while syote >= 0:
    tulos_lit = gallon_litra(syote)
    print(f'{syote} gallonaa on {tulos_lit} litraa')

    syote = float(input('anna bensan määrä gallonina: '))'''

#4

'''def laske_summa(lista):
    yht = 0

    for luku in lista:
        yht += luku

    return yht


testil = [5, 10, 15, 20]

listas = laske_summa(testil)
print(f'listan lukujen summa on : {listas}')'''

#5

'''def karsi_parittomat(alk_lista):
    parilliset = []

    for luku in alk_lista:
        if luku % 2 == 0:
            parilliset.append (luku)
    return parilliset

mun_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
karsittu = karsi_parittomat(mun_lista)

print(f'alkuperäinen lista {mun_lista}')
print(f'karsittu lista (vain parilliset): {karsittu}')'''

#6

import math

def laske_ykshinta(halkaisijacm, hinta_e):
#muunnetaan halkaisija säteeksi ja cm -> m
    sade_m = halkaisijacm / 200
#lasketaan pinta alaksi
    pa_m2 = math.pi * (sade_m ** 2)

    yksikkohinta = hinta_e / pa_m2
    return yksikkohinta

#pääohjelma

halk1 = float(input("anna 1. pizzan halkaisija cm:" ))
hin1 = float(input("anna 1. pizzan hinta €: "))

halk2 = float(input("anna 2. pizzan halkaisija cm:" ))
hin2 = float(input("anna 2. pizzan hinta €: "))

yksh1 = laske_ykshinta(halk1, hin1)
yksh2 = laske_ykshinta(halk2, hin2)

if yksh1 < yksh2:
    print("1. pizza antaa paremman vastineen rahalle")
elif yksh1 > yksh2:
    print("2. pizza antaa paremman vastineen rahalle")
else:
    print("Pizzoilla on täsmälleen sama yksikköhinta")