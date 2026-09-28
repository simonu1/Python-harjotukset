class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi
 # kirja aliluokka, perii julkaisun
class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        super().__init__(nimi)
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        print(f"Kirjan nimi: {self.nimi}")
        print(f"Kirjoittaja: {self.kirjoittaja}")
        print(f"Sivumäärä: {self.sivumaara} sivua")

# lehti aliluokka, perii julkaisun
class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        super().__init__(nimi)
        self.paatoimittaja  = paatoimittaja

    def tulosta_tiedot(self):
        print(f'lehden nimi: {self.nimi}')
        print(f'päätoimittaja: {self.paatoimittaja}')

#pääohjelma

if __name__ == "__main__":
    aku_ankka = Lehti("aku ankka", "aki hyyppä")
    hytti_nro_6 = Kirja("hytti n:o 6", "rosa liksom", 200)

aku_ankka.tulosta_tiedot()
hytti_nro_6.tulosta_tiedot()
