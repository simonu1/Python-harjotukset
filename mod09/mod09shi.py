'''''''''k1_rotu = "kultainen noutaja"
k1_nimi = "töhö"
k1_syntymavuosi = 2021

k2_rotu = "labradori"
k2_nimi = "jouko"
k2_syntymavuosi = 2024

k3_rotu = "pitbull"
k3_nimi = "pekka"
k3_syntymavuosi = 2026

class koira:
    pass

koira = koira()
koira2 = koira()

koira.nimi = "töhö"
koira.rotu = "kultainen noutaja"

koira2.nimi = "jouko"
koira2.rotu = "labradori"

print("ensimmäisen koiran nimi", koira.nimi)
print("ensimmäisen koiran rotu", koira.rotu)

print("toisen koiran nimi", koira2.nimi)
print("toisen koiran rotu", koira2.rotu)
'''
'''

class Koira:

tehty = 0

    def __init__(self, nimi, rotu, syntymävuosi, haukahdus="vuhvuh"):
        self.nimi = nimi
        self.rotu = rotu
        self.syntymävuosi = syntymävuosi
        self.haukahdus = haukahdus
        self.luokitus = "nisäkäs"
        Koira.tehty += 1
koira = Koira("töhö", "kultainen noutaja")
koira2 = Koira("jouko", "labrador")

def hauku(self, kerrat):
        for x in range(kerrat):
            print(self.haukahdus)

koira = Koira("lissu", "bokseri", 2022, "hauhau")
koira2 = Koira("jouko", "puudeli", 2025, "hau")
koira3 = Koira("jari", "terrier", 2021, "hauhauhau")

print(f'1. koiran nimi{koira.nimi} ja rotu {koira.rotu}')
print(f'2. koiran nimi{koira2.nimi} ja rotu {koira2.rotu}')

'''
print()
print('------------------')
info = 'pelaajan tiedot'


class Player:
    def __init__(self, name, skilllvl, inv):
        self.name = name
        self.skilllvl = skilllvl
        self.inv = inv

    def show_info(self):
        print(info)
        print('pelaajan nimi', self.name)
        print('taso', self.skilllvl)
        for item in self.inv:
            print('-------')

    def add_item(self, item):
        self.inv.add(item)


p1 = Player('p1', 10, ('map', 'knife'))
p2 = Player('p2', 15, ('map', 'sword'))

print(f'pelaajan 1 nimi on {p1.name} ja taso on {p1.skilllvl}')
