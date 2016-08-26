import random


def juego(n):
    secreto = random.choice(range(n * 10))
    intentos = []
    intento = -1
    while intento != secreto:
        try:
            intento = int(input('Adiviná: '))
        except:
            continue
        intentos.append(intento)
        if intento > secreto:
            print('Más chico!')
        else:
            print('Más grande!')

    print('Adivinaste!')
    print('Intentos: {0}'.format(intentos))

try:
    nivel = int(input('Nivel: '))
except:
    nivel = 1
juego(nivel)
