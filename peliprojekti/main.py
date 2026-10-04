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
            tulokset = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        tulokset = []
        #jos tätä tiedostoa ei ole tai se on viallinen, aloitetaan tyhjällä listalla.
        
        tulokset.append({"nimi": nimi, "pisteet": pisteet})

        tulokset = sorted(tulokset, key=lambda x: x["pisteet"], reverse=True)
        tulokset = tulokset[:5]
        
        with open("highscores.json", "w") as file:
            json.dump(tulokset, file, indent=4)

def nayta_high_score():
    #päävalinkon #4 kohtaan, tiedoston lukeva ja tulostava funktio
    print("\n --- Top 5 HIGH SCORES ---")
    try:
        with open("highscores.json", "r") as file:
            tulokset = json.load(file)

        if not tulokset:
            print("lista on vielä tyhjä")
        else:
            for i, tulos in enumerate(tulokset, 1):
                print(f'{i}. {tulos["nimi"]}: {tulos["pisteet"]} pistettä')
    except FileNotFoundError:
            print("lista on vielä tyhjä")
    print("------------------------------------------")

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
    print('Etsi roskia 7x7 ruudukosta ja vie')
    print('ne ruutuun 7-7 kierrätettäväksi.')
    print(" kirjoita 'esc' pysäyttääksesi pelin")

    #7x7 ruudukko Huone-olioita heti pelin alussa
    kartta = []
    for y in range(7):
        rivi = []
        for x in range(7):
            uusi_huone = Huone(f"Ruutu {x+1}-{y+1}")
            rivi.append(uusi_huone)
        kartta.append(rivi)

    # määritetään roskien määrä tason mukaan, taso 1 sisältää 3 roskaa, taso 2 sisältää 4 roskaa, taso 3 sisältää 5 roskaa
    roska_lkm = 0
    kartalla_olevat_roskat = 2 + pelaaja.taso

    while roska_lkm < kartalla_olevat_roskat:
        rx = random.randint(0,6)
        ry = random.randint(0,6)

        if (rx, ry) != (3, 3) and (rx, ry) != (6, 6) and kartta[ry][rx].esine is None:
            roska_tyypit = [
                ("muovipullo", 0.2),
                ("tölkki", 0.1),
                ("pahvilaatikko", 0.4),
                ("vahna akku", 2.5)
            ]
            valittu_roska = random.choice(roska_tyypit)

            kartta[ry][rx].esine = esine(valittu_roska[0], valittu_roska[1])
            roska_lkm += 1

    #indeksit 6,6 (ruutu 7-7) tehdään kierrätyskeskukseksi
    kartta[6][6].nimi = "kierrätyskeskus"

    #aloituspiste 7x7 ruudukon keskelle, 0-6, eli 3 on keskipiste
    pelaaja_x = 3
    pelaaja_y = 3
    pelaaja.sijainti = kartta[pelaaja_y][pelaaja_x]

    while peli_käynnissa:
        print(f'\nOlet tällä hetkellä paikassa: {pelaaja.sijainti.nimi}')

        if pelaaja.sijainti.esine is not None:
            roska = pelaaja.sijainti.esine
            print(f' !! löysit maasta roskan: {roska.nimi} ({roska.paino}kg)')
            roska_valinta = input("Poimitko roskan? (k/e): ").strip().lower()
            if roska_valinta == 'k':
                pelaaja.lisaa_esine(roska)  
                pelaaja.lisaa_pisteita(10)
                pelaaja.sijainti.esine = None
       
        elif pelaaja_x == 6 and pelaaja_y == 6:
            print("\n--- Saavuit Kierrätyskeskukseen ---")
            kerätyt = len(pelaaja.inventory)
            print(f"Toit mukanasi {kerätyt} roskaa. Tason läpäisyyn vaaditaan vähintään 2 roskaa.")

            if kerätyt >= 2:
                print(f' aloitetaan roskien lajittelu')
                for e in pelaaja.inventory:
                    print(f'- Lajittelit esineen "{e.nimi}" konttiin!')

                    #pistesysteemi 
                    taso_bonus = pelaaja.taso * 100
                    roska_bonus = kerätyt * 50 
                    pelaaja.lisaa_pisteita(taso_bonus + roska_bonus)

                    pelaaja.inventory.clear()
                    print("Reppusi oon nyt tyhjenny ja roskat viety")

                    paivita_high_score(pelaaja.nimi, pelaaja.pisteet)
                    

                if pelaaja.taso > 3:
                    print("\n" + "="*20)
                    print(" Onneksi olkoon, läpäisit pelin kaikki tasot ")
                    print(f" Lopulliset pisteesi: {pelaaja.pisteet}")
                    print("="*50)
                    paivita_high_score(pelaaja.nimi, pelaaja.pisteet)
                    peli_käynnissa = False

                    print("\n" + "="*20)
                    print(f' Loistavaa, läpäisit tason')
                    if pelaaja.taso == 2:
                        print('pääsit tasolle 2!')
                        print('Kartalla on nyt 4 roskaa')
                    
                    elif pelaaja.taso == 3:
                        print(" Pääsit viimeiselle tasolle! ")
                        print(" Kartalla on nyt 5 roskaa kerättävänä.")
                    print(" Sinut siirretään takaisin aloitukseen.")
                    
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
                print("3. tallenna peli tiedostoon")
                print("lopeta - Palaa päävalikkoon")

                tauko_valinta = input("\nAnna komento: ").strip().lower()

                if tauko_valinta == '1':
                    print("Jatketaan peliä...\n")
                    peli_tauolla = False
                elif tauko_valinta == '2':
                    print("\n--- REPUN SISÄLTÖ ---")
                    nayta_inventaario(pelaaja.inventory)
                    print("--------------------\n")
                elif tauko_valinta == '3':
                    pelaaja.tallenna_peli()
                    print("--------------------\n")
                elif tauko_valinta == 'lopeta':             
                    print("Palataan päävalikkoon.")

                    paivita_high_score(pelaaja.nimi, pelaaja.pisteet)
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

#päävalikon ohjelma
name = input("anna nimesi: ")
age = int(input("kuinka vanha olet:"))

if age < 12:
    print('olet alaikäinen, ohjelma sammuu.')
else:
    print("hei", name)
    pelaaja = Pelaaja(name, age)

    try:
        with open("peliprojekti/intro.txt", "r", encoding="utf-8") as file:
            print(file.read())
    except FileNotFoundError:
        print("\nEsittelytekstia (intro.txt) ei loytynyt!")    
        
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
            if pelaaja.lataa_peli():
                pelaa_pelia(pelaaja)
        elif komento == '3':
            try:
                with open("peliprojekti/ohjeet.txt", "r", encoding="utf-8") as file:
                    print(file.read())
            except FileNotFoundError:
                print("\nOhjetiedostoa (ohjeet.txt) ei löytynyt!")

        elif komento == '4':
            nayta_high_score()
        else:
            print('tuntematon komento, yritä uudestaan')