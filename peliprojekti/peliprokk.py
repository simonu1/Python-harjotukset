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