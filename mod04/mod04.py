import random

# kolikonheittosimulaattori
random_number = random.randint(0,1)
print(random_number)

#if lauseen _ehto_ muodostuu AINA true tai false arvoksi
if random_number == 0:
    result = "kruuna"
    print("kruuna tuli")
else:
    result = "klaava"


print(f"heitit kolikkoa ja sait {result}n.")


# kolikonheittosimulaattori 2.0

random_number = random.random()
print(random_number)

# kolikko jää pystyyn todnäk. 1/100

if random_number < 0.01:
    print("kolikko jäi pystyyn")
elif random_number < 0.505:
    print("kruuna tuli")
else:

    print("klaava tuli")

##erilaisia ehtoja 

arvo = 100

print(69  >arvo> 150 )
print(100 != 101)

ikä = int(input("anna ikä: "))
if 15 <= ikä < 18:
    paino = float(input("anna paino (kg)"))

if ikä >= 18 or ikä >= 15 and paino >= 55:
    print("lääkkeen käyttö sallittua")

print(True or {True and False})

