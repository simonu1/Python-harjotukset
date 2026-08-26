#tehtävä 1
'''kuhap = float(input("anna kuhan pituus: "))

if kuhap <37:
   kuhalyhyt = 37 - kuhap
print(f"vapauta kuha veteen, kuha on {kuhalyhyt} cm liian lyhyt")
'''
#tehtävä 2

'''print("anna hyttiluokat: \n"
    "LUX on parvekkeellinen hytti yläkannella.\n"
    "A on ikkunallinen hytti autokannen yläpuolella.\n"
    "B on ikkunaton hytti autokannen yläpuolella.\n"
    "C on ikkunaton hytti autokannen alapuolella.\n")
hyttiluoka = input("anna hyttiluokka:")
if hyttiluoka in ("LUX", "A", "B", "C"):
    print("kiitos")
else:
    print("virheellinen hyttiluokka")
'''
#tehtävä 3

'''sukupuoli = input("anna sukupuoli: mies/nainen\n")
hmg = float (input("anna hemoglobiiniarvo (g/l)\n"))

if sukupuoli == "nainen":
    if hmg <117:
        print("hemoglobiini (g/l) on alhainen")
    elif hmg >175:
        print("hemoglobiini (g/l) on korkea")
    else:
        print("hemoglobiini (g/l) on normaali")

elif sukupuoli == "mies":
    if hmg <134:
        print("hemoglobiini (g/l) on alhainen")
    elif hmg >195:
        print("hemoglobiini (g/l) on korkea")
    else:
        print("hemoglobiini (g/l) on normaali")
'''

#tehtävä 4

vsl = float(input("anna vuosiluku:\n"))
if (vsl % 400 == 0) or (vsl % 4 == 0 and vsl % 100 != 0):
    print(f"{vsl:.0f} on karkausvuosi")
else:
    print(f"{vsl:.0f} ei ole karkausvuosi")