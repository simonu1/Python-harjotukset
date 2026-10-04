import json

class esine:
    #Yksittäinen inventaarioon lisättävä esine.

    def __init__(self, nimi: str, paino: float):
        self.nimi = nimi
        self.paino = paino

    def keraa(self):
        #Käytä esinettä ja palauta käyttäjälle ilmoitettava viesti.
        return f'Keräsit esineen: {self.nimi}'

    def tiedot(self):
        #Palauta esineen nimi
        if self.paino:
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

    #liikkumis funktio
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