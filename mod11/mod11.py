class Elain:

    elainten_lkm = 0

    def __init__(self, nimi, paino, syntaik):
        self.nimi = nimi
        self.paino = paino
        self.syntaik = syntaik

    def liiku(self):
        print(f'{self.nimi} liikkuu johonkin')

    def kaikki_tiedot(self):
        print(f'nimi {self.nimi}, paino {self.paino/1000}kg, syntymäaika {self.syntaik}')

class Peto:
    def __init__(self, on_metsastaja):
        self.on_metsastaja = on_metsastaja

class Ilves(Elain):
    
    def kilju(self):
        print(f'ilves nimeltä {self.nimi} kiljuu!')

    def kaikki_tiedot(self):
        print('\nIlves')
        super().kaikki_tiedot()
    
class Karhu(Elain, Peto):
    def __init__(self, nimi, paino, syntaik, on_horroksessa):
        self.on_horroksessa = on_horroksessa
        Elain.__init__(self, nimi, paino, syntaik)
        Peto.__init__(self.on_metsastaja)

    def karju(self):
        print(f'karhu nimeltä {self.nimi} karjuu')

    def liiku(self):
        print(f'karhu {self.nimi} myörii eteenpäin')

    def kaikki_tiedot(self):
        print(f'\nkarhu on metsastaja: {self.on_metsastaja}, joka on nyt talviunilla{self.on_horroksessa}')
        super().kaikki_tiedot()
