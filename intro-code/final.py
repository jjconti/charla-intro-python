import random

vidas = {1: 3, 2: 5, 3: 8}


def game_over():
    print("*" * 8)
    print("game over".upper())
    print("*" * 8)
    exit()


def pistas(intento, secreto, intentos):
    vidas_restantes = vidas.get(nivel, 10) - intentos
    if intento > secreto:
        print('Más chico! ({})'.format(vidas_restantes))
    else:
        print('Más grande! ({})'.format(vidas_restantes))

def juego(n):
    secreto = random.choice(range(n * 10))
    intentos = []
    intento = -1
    while intento != secreto:
        cadena = input('Adiviná: ')
        if cadena == 'salir':
            exit()
        try:
            intento = int(cadena)
        except:
            print("Poné un número!!! (salamin)")
            continue
        intentos.append(intento)
        if len(intentos) >= vidas.get(n, 10):
            game_over()
        if intento != secreto:
            pistas(intento, secreto, len(intentos))

    print('Adivinaste!')
    print('Intentos: {0}'.format(intentos))

try:
    nivel = int(input('Ingrese el nivel: '))
except:
    nivel = 1

MAX_NIVEL = 10

jugó = False


def chorro():
    archivo = open('gasper.txt')
    print(archivo.read())
    exit()


while True:
    if nivel > MAX_NIVEL:
        if jugó:
            chorro()
        else:
            nivel = 1
    print("*" * 8)
    print("NIVEL: {}".format(nivel))
    print("*" * 8)
    juego(nivel)
    jugó = True
    nivel = nivel + 1

