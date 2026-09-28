class Pelaaja:
    def __init__(self, nimi, palvelin):
        self.nimi = nimi
        self.palvelin = palvelin

    def viestittele(self, viesti):
        print(f'[{self.nimi}-{self.palvelin}]')