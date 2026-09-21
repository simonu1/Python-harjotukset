vuodenajat = ('talvi', 'kevät', 'kesä', 'syksy')

kk = int(input('anna kuukausi: (1-12)'))

if kk in (12, 1, 2):
    va = 0 # talvi
elif kk in (3, 4, 5):
    va = 1
elif kk in (6, 7, 8):
    va = 2
elif kk in (9, 10, 11):
    va = 3
else:
    va = None

if va is not None:
    print(f'kuukausi {kk}, vuodenaika on {vuodenajat[va]}')
else:
    print('virheellinen kuukausi')

nimet = set()

while True:
    nimi = input('anna nimi: ')

    if nimi == "":
        break

    if nimi in nimet:
        print('aijemmin syötetty nimi')
    else:
        nimet.add(nimi)

print('\nsyötetyt nimet: ')
for nimi in nimet:
    print(nimi)

lentoasemat = {}

while True:
    print('\nvalitse toiminto: ')
    print('1 - syötä uusi lentoasema')
    print('2 - hae lentoaseman tiedot')
    print('3 - lopeta')
    x = input('1, 2, 3: ')

    if x == '1':
        icao = input('anna icao koodi:').upper()
        nimi = input('anna lentoaseman nimi: ')
        lentoasemat[icao] = nimi
        print(f'lentoasmea {nimi}, {icao} tallennettu')

    elif x == '2':
        icao = input("anna icao koodi: ").upper()

    if icao in lentoasemat:
        print(f'icao-koodia {icao} vastaava asema on: {lentoasemat[icao]}')
    else:
        print(f' {icao} koodia vastaavaa aseemaa ei ole tallennettu')

    if x =='3':
        print('ohjelma päättyy')
        break
