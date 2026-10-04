import random
import json
# luokat.py:stä importataan esine, huone, ja pelaaja funktiot
from luokat import esine, Huone, Pelaaja

def tervehdi(pelaajanimi):
    print(f'terve {pelaajanimi}')

def paivita_high_score(nimi, pisteet):
    #tämä tallentaa pelaajan tuloksen high score listalle
    tiedosto = "highscores.json"

    try:
        with open(tiedosto, "r") as file: 
            json.dump(tulokset, file, indent=4)
    except (FileNotFoundError, json.JSONDecodeError):
        tulokset = []
        #jos tätä tiedostoa ei ole tai se on viallinen, aloitetaan tyhjällä listalla.
        
        tulokset.append({"nimi": nimi, "pisteet": pisteet})

        tulokset = sorted(tulokset, key=lambda x: x["pisteet"], reverse=True)
        tulokset = tulokset[:5]
        
        with open("highscores.json", "w") as file:
            json.dump(tulokset, file, indent=4)

def nayta_inventaario(inventory=None):
    """Näytä pelaajan inventaarion sisältö."""
    if not inventory:
        print('Inventaario on tyhjä.')
        return

    for esine in inventory:
        print(f'- {esine}')


def pelaa_pelia(pelaaja):
    peli_käynnissa = True
    print('tervetuloa peliin')
    print(" 'esc' pysäyttääksesi pelin")

    #7x7 ruudukko Huone-olioita heti pelin alussa
    kartta = []
    for y in range(7):
        rivi = []
        for x in range(7):
            uusi_huone = Huone(f"Ruutu {x+1}-{y+1}")
            rivi.append(uusi_huone)
        kartta.append(rivi)

    #aloituspiste 7x7 ruudukon keskelle, 0-6, eli 3 on keskipiste
    pelaaja_x = 3
    pelaaja_y = 3
    pelaaja.sijainti = kartta[pelaaja_y][pelaaja_x]

    while peli_käynnissa:
        print(f'\nOlet tällä hetkellä paikassa: {pelaaja.sijainti.nimi}')
        print('valitse minne mennään (e / t / o / v)')
        valinta = input('anna komento: ').strip().lower()

        if valinta == 'e':
            if pelaaja_y < 6:
                pelaaja_y += 1
                pelaaja.sijainti = kartta[pelaaja_y][pelaaja_x]
                print(f'liikuit huoneeseen: {pelaaja.sijainti.nimi}')
            else:
                print('aita vastassa itään!')
        elif valinta == 't':
            if pelaaja_y > 0:
                pelaaja_y -= 1
                pelaaja.sijainti = kartta[pelaaja_y][pelaaja_x]
                print(f'liikuit huoneeseen: {pelaaja.sijainti.nimi}')
            else:
                print('aita vastassa pohjoisessa!')
        elif valinta == 'o':
            if pelaaja_x < 6:
                pelaaja_x += 1
                pelaaja.sijainti = kartta[pelaaja_y][pelaaja_x]
                print(f'liikuit huoneeseen: {pelaaja.sijainti.nimi}')
            else:
                print('Seinä vastassa idässä!')
        elif valinta == 'v':
            if pelaaja_x > 0:
                pelaaja_x -= 1
                pelaaja.sijainti = kartta[pelaaja_y][pelaaja_x]
                print(f'liikuit huoneeseen: {pelaaja.sijainti.nimi}')
            else:
                print('Seinä vastassa lännessä!')
        elif valinta == 'esc':
            peli_tauolla = True
            print("\n--- PELI ON TAUOLLA ---")

            while peli_tauolla:
                print("1. Jatka peliä")
                print("2. Katso inventaario")
                print("lopeta - Palaa päävalikkoon")

                tauko_valinta = input("\nAnna komento: ").strip().lower()

                if tauko_valinta == '1':
                    print("Jatketaan peliä...\n")
                    peli_tauolla = False
                elif tauko_valinta == '2':
                    print("\n--- REPUN SISÄLTÖ ---")
                    nayta_inventaario(pelaaja.inventory)
                    print("--------------------\n")
                elif tauko_valinta == 'lopeta':
                    print("Palataan päävalikkoon.")
                    peli_tauolla = False
                    peli_käynnissa = False
                else:
                    print("Tuntematon komento.")

            else:
                print("tuntematon suunta, anna e / t / o / v tai esc")

    # 7x7 kartta huone oliosta pelifunktion alusta
    kartta = []
    for y in range(7):
        rivi = []
        for x in range(7):
            uusi_huone = Huone(f'ruutu {x+1}-{y+1}')
            rivi.append(uusi_huone)
        kartta.append(rivi)

    kartta[2][1].esine = esine()

#päävalikon ohjelma
name = input("anna nimesi: ")
age = int(input("kuinka vanha olet:"))

if age < 12:
    print('olet alaikäinen, ohjelma sammuu.')
else:
    print("hei", name)
    pelaaja = Pelaaja(name, age)

    while True:
        print('\nPäävalikko')
        print('1. Aloita peli')
        print('2. Lataa peli')
        print('3. Ohjeet')
        print('4. Katso parhaat tulokset')
        print('5. lopettaaksesi pelin')

        komento = input('\nAnna komento: ')
        if komento == "5":
            print('ohjelma lopetetaan')
            break
        elif komento == '1':
            print('Aloitetaan peli')
            pelaa_pelia(pelaaja)
        elif komento == '2':
            print('Ladataan peli')
        elif komento == '3':
            print('\n---- Pelin ohjeet ----')
            print('Tässä pelissä teet valintoja, joilla sinun täytyy läpäistä taso.')
            print('Peli koostuu useammasta tasosta, jotka pitää läpäistä voittaaksesi!')
        elif komento == '4':
            print('näytetään tulokset (luetaan tiedosto)...')
        else:
            print('tuntematon komento, yritä uudestaan')