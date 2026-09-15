class Auto:
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
print("auton nopeus kiihdytyksen jälkeen", auto.nopeus)
auto.kulje(1.5)
auto.kiihdytä(-200)
print("auton nopeus kiihdytyksen jälkeen", auto.nopeus)
print("kuljettu matka", auto.km)
