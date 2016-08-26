import random


def juego(n):
    secreto = random.choice(range(n * 10))
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

nivel = int(input('Nivel: '))
juego(nivel)
