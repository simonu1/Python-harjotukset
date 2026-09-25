"""class Hissi:
    def __init__(self, tunniste, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.nykyinen = alin_kerros
        self.tunniste = tunniste

    def kerros_ylos(self):
        if self.nykyinen < self.ylin:
            self.nykyinen += 1
        print(self.nykyinen)

    def kerros_alas(self):
        if self.nykyinen > self.alin:
            self.nykyinen -= 1
        print(self.nykyinen)

    def siirry_kerrokseen(self, kohdekerros):
        print(f'siirrytään kerrokseen {kohdekerros}')
        while self.nykyinen < kohdekerros:
            self.kerros_ylos()
        while self.nykyinen > kohdekerros:
            self.kerros_alas()

class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.hissit = []
       
        for x in range(hissien_lkm):
            uusi_hissi = Hissi(f'numero {x+1}', alin_kerros, ylin_kerros)
            self.hissit.append(uusi_hissi)

    def aja_hissia(self, numero, kohdekerros):
        print(f'ajetaan hissiä {numero} kerrokseen {kohdekerros}')

    def palohaly(self):
        print("palohälys!") 
        #h = hissi olio
        for h in self.hissit:
            h.siirry_kerrokseen(h.alin)

talo = Talo(2, 13, 3)

talo.aja_hissia(1, 5)
talo.aja_hissia(1, 7)
talo.aja_hissia(3, 2)
talo.aja_hissia(3, 8)

talo.palohaly()

#pääohjelma

hissi1 = Hissi("Pääaula 1", 1, 12)
hissi2 = Hissi("Henkilökunta", 5, 20)
print(hissi1.nykyinen)
print(hissi2.nykyinen)

hissi1.siirry_kerrokseen(8)
hissi2.siirry_kerrokseen(15)
hissi1.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(5)
hissi2.siirry_kerrokseen(5)
hissi1.siirry_kerrokseen(1)

"""