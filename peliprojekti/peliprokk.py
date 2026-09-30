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

class Pelaaja:
    def __init__(self, nimi, ika):
        self.nimi = nimi
        self.ika = ika
        self.pisteet = 0
        self.inventory =[]
        self.x = 4
        self.y = 4

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
            
    #pelitilanteen tallennus
    def tallenna_peli(self):
        print('tallennetaan peli')

    def lataa_peli(self):
        pass




#tyhjä lista esineille
inventory = []

def tervehdi(ppelaajanimi):
    print(f'terve {ppelaajanimi}')

def lisaa_esine():
    nimi = input("lisää esine inventaarioon: ")
    uusi_esine = esine(nimi, "")
    inventory.append(uusi_esine)
    print(f'lisätty: {uusi_esine}')

def nayta_inventaario():
    print('\n-- inventaarion sisältö-- ')
    if not inventory:
        print("inventaario on tyhjä")
    else:
        x = 1
        for esine in inventory:
            print(f'{x}. {esine}')
            x += 1
    print('-------------------------------------------')


def pelaa_pelia():
    peli_käynnissa = True
    print('tervetuloa peliin')
    print(" 'esc' pysäyttääksesi pelin")

    while peli_käynnissa:
        print('valitse minne mennään (e / t / o / v)')
        valinta = input('anna komento: ').strip().lower()

        if valinta == 'e':
            print('jatketaan eteenpäin...')

        elif valinta == 't':
            print('peruutetaan takaisin...')

        elif valinta == 'o':
            print('käännytään oikealle...')

        elif valinta == 'v':
            print('käännytään vasemmalle...')

        elif valinta == "esc":
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
                    nayta_inventaario()
                    print("--------------------\n")
                elif tauko_valinta == 'lopeta':
                    print("Palataan päävalikkoon.")
                    peli_tauolla = False
                    peli_käynnissa = False
                else:
                    print("Tuntematon komento.")


#päävalikon ohjelma
name = input("anna nimesi: ")
age = int(input("kuinka vanha olet:"))

if age < 12:
    print('olet alaikäinen, ohjelma sammuu.')
else:
    print("hei", name)

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
            pelaa_pelia()
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