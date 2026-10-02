import json
import random

class esine:
    #Yksittäinen inventaarioon lisättävä esine.

    def __init__(self, nimi, kuvaus):
        self.nimi = nimi
        self.kuvaus = kuvaus

    def kayta(self):
        #Käytä esinettä ja palauta käyttäjälle ilmoitettava viesti.
        return f'Käytit esinettä: {self.nimi}'

    def tiedot(self):
        #Palauta esineen nimi
        if self.kuvaus:
            return f'{self.nimi}'
        return self.nimi

    def __str__(self):
        return self.tiedot()

class Huone:
    def __init__(self, nimi, esine=None):
        self.nimi = nimi
        self.esine = esine # voi olla esine olio, tai jos huone on tyhjä, niin none

class Pelaaja:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.pisteet = 0
        self.inventory =[]
        self.x = 4
        self.y = 4
        self.taso = 1

    def lisaa_pisteita(self, maara):
        self.pisteet += maara
        print(f'sait {maara} pisteen! Pisteet yhteensä: {self.pisteet}!')

    def info(self):
        print(f'pelaajan ikä on {self.ika} ja pisteet {self.pisteet}')

    def liiku_eteen(self):
        if self.y < 7:
            self.y += 1
            print("liikut askeleen eteenpäin")
        else:
            print('aita vastassa pohjoisessa!')

    def liiku_taakse(self):
            if self.y > 7:
                self.y -= 1
                print("liikut askeleen taaksepäin")
            else:
                print('aita vastassa etelässä!')

    def liiku_oikealle(self):
        if self.x < 7:
            self.x += 1
            print("Otat askeleen oikealle.")
        else:
            print('Seinä vastassa idässä!')
    
    def liiku_vasemmalle(self):
        if self.x > 1:
            self.x -= 1
            print("Otat askeleen vasemmalle.")        
        else:
            print("Seinä vastassa lännessä!")

    def liiku(self, uusi_huone):
        self.sijainti = uusi_huone
        print(f'liikuit huoneeseen: {self.sijainti.nimi}')

    def lisaa_esine(self, uusi_esine):
        self.inventory.append(uusi_esine)
        print(f'keräsit esineen: {uusi_esine.nimi}')


    #pelitilanteen tallennus

    def tallenna_peli(self):
        print('tallennetaan peli')
        try:
            with open("save.txt", "w") as file:
                data = {
                    "nimi": self.nimi,
                    "ika": self.ika,
                    "pisteet": self.pisteet,
                    "x": self.x,
                    "y": self.y,
                    "taso": self.taso
                }
                json.dump(data, file)
            print("peli tallennettu!")
        except FileNotFoundError:
            print("Tiedostoa ei löydy.")
        except IOError:
            print("Tiedoston käsittelyssä tapahtui virhe.")

    #pelitilanteen lataaminen
    
    def lataa_peli(self):
        print('ladataan peli.')
        try: 
            with open("save.txt", "r") as file:
                data = json.load(file)

                self.nimi = data["nimi"]
                self.ika = data['ika']
                self.pisteet = data['pisteet']
                self.x = data['x']
                self.y = data['y']
                self.taso = data['taso']
            print("Peli ladattu onnistuneesti!")
            return True
        except FileNotFoundError:
            print("Tiedostoa ei löydy, ei tallennettua peliä")
            return False
        except IOError:
            print('Tiedoston käsittelyssä tapahtui virhe')
            return False

def tervehdi(pelaajanimi):
    print(f'terve {pelaajanimi}')


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

    kartta[2][1].esine = Esine()

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