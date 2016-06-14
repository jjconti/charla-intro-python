import random

secreto = random.choice(range(10))
intentos = []
intento = int(input('Adiviná: '))
while intento != secreto:
    intentos.append(intento)
    if intento > secreto:
        print('Más chico!')
    else:
        print('Más grande!')
    intento = int(input('Adiviná: '))

print('Adivinaste!')
print('Intentos: {0}'.format(intentos))
