class esine:
    #Yksittäinen inventaarioon lisättävä esine.

    def __init__(self, nimi):
        self.nimi = nimi
        

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


#tyhjä lista esineille
inventory = []

def tervehdi(pnimi):
    print(f'terve {pnimi}')

def lisaa_esine():
    nimi = input("lisää esine inventaarioon: ")
    uusi_esine = esine(nimi)
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

def lebron_highlights():
    print('lebron highlights joskus!')




#pääohjelma
name = input("anna nimesi: ")
age = int(input("kuinka vanha olet:"))
print("hei", name)

if age < 12:
    print('olet alaikäinen, ohjelma sammuu.')
else:
    print("hei", name)

    while True:
        print('\nPäävalikko')
        print('1. noomorjest')
        print('2. lebroooon')
        print('kirjoita "lopeta" lopettaaksesi')

        komento = input('\nAnna komento: ')
        if komento == "lopeta":
            print('ohjelma lopetetaan')
            break
        elif komento == '1':
            print(f'moro {name}.')
        elif komento == '2':
            print('lebron highlights joskus!')
        else:
            print('tuntematon komento, yritä uudestaan')