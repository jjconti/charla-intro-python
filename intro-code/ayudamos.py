import random

secreto = random.choice(range(21))

intento = int(input('Adiviná: '))
while intento != secreto:
    if intento > secreto:
        print('Más chico!')
    else:
        print('Más grande!')
    intento = int(input('Adiviná: '))

print('Adivinaste!')
