import random

secreto = random.choice([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

intento = int(input('Adiviná: '))
while intento != secreto:
    if intento > secreto:
        print('Más chico!')
    else:
        print('Más grande!')
    intento = int(input('Adiviná: '))

print('Adivinaste!')
