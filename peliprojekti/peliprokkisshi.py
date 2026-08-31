peli_käyn = True
# main loop
print('tervetuloa peliin')

while peli_käyn:
    print('valitse minne mennään (j/l)')
    # j jatkaa, l lopettaa
    valinta = input('anna komento: ')
    if valinta == 'j':
        print('jatketaan')
    elif valinta == 'l':
        print("lopetit pelin")
        peli_käyn = False