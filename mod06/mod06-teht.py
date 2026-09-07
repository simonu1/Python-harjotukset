import random

#1

'''nm= int(input('anna arpakuutioiden määrä: '))

summa = 0 

for i in range(nm):
    heitto = random.randint(1,6)
    summa += heitto

print(f'lukujen summa on: {summa}')
'''
#2
'''
nums = []

while True:
    input_num = input("anna luku: ")
    if input_num == "":
        #lopeta kysely
        break
    #lisätään syötetty luku listalle
    nums.append(int(input_num))
nums.sort(reverse=True)

#print(nums[0:5])

#for lauseella
for num in range(5):
    print(nums[num])'''

#3

'''luku = int(input('anna kokonaisluku: '))

al = True

if luku < 2: 
    al = False

else: 
    for i in range(2, luku):
        if luku % i == 0:
            al = False
            break

if al:
    print(f'luku {luku} on alkuluku')
else: 
    print(f'luku {luku} ei ole alkuluku')'''

#4
'''
kaupungit = []

for i in range(5):
    name = input('anna kaupungi: ')
    kaupungit.append(name)

for kaupunki in kaupungit:
    print(kaupunki)'''