'''class Auto:
    def __init__(self, rek, huippunop, nopeus, km):
        self.rek = rek
        self.huippunop = huippunop
        self.nopeus = nopeus
        self.km = km

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunop:
            self.nopeus = self.huippunop
        elif self.nopeus < 0:
            self.nopeus = 0
        return self.nopeus

    def kulje(self, tunnit):
        self.km += self.nopeus * tunnit
        return self.km

auto = Auto('abc-123', 142, 0, 0)

print('auton rekisteritunnus', auto.rek)
print('huippunopeus', auto.huippunop)
print('nopeus', auto.nopeus)
print('kuljettu matka', auto.km)

auto.kiihdytä(30)
auto.kiihdytä(70)
auto.kiihdytä(50)
auto.km = 2000
print("auton nopeus kiihdytyksen jälkeen", auto.nopeus)
auto.kulje(1.5)

print("auton nopeus kiihdytyksen jälkeen", auto.nopeus)
print("kuljettu matka", auto.km)
print(f' ennen ajoa nopeus: {auto.nopeus} km/h, ja matka {auto.km} km')'''

import random

class Auto:

    def __init__(self, rek, huippunop):
        self.rek = rek
        self.huippunopeus = huippunop
        self.nopeus = 0
        self.km = 0 

    def kiihdytä(self, muutos):
        self.nopeus += muutos
        if self.nopeus > self.huippunopeus:
            self.nopeus = self.huippunopeus
        elif self.nopeus < 0:
            self.nopeus = 0
        return self.nopeus

    def kulje(self, tunnit):
        self.km += self.nopeus * tunnit
        return self.km

autot =[]
for x in range(1, 11):
    rek = f'ABC{x}'

    huippu = random.randint(100, 200)
    autot.append(Auto(rek, huippu))

kilpailu_käynnissä = True
tunnit = 0
while kilpailu_käynnissä:
    tunnit += 1

    for auto in autot:
        muutos = random.randint(-10,15)
        auto.kiihdytä(muutos)

        auto.kulje(1)

        if auto.km >= 10000:
            kilpailu_käynnissä = False

print(f'kilpailu loppui, aikaa kului {tunnit} tuntia.')
print(f"{'rekisteritunnus':<16} | {'huippunopeus':<15} | {'loppunopeus':<15} | {'matka':<12}")
print('--------------------------------------------')

for auto in autot:
    print(f"{auto.rek:<16} | {auto.huippunopeus:<11} km/h | {auto.nopeus:<9} km/h | {auto.km:<12.1f} km")