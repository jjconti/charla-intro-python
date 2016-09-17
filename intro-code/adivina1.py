secreto = 5
mensaje = 'Diga un n del uno al diez: '
dichos = []

while int(input(mensaje)) != secreto:
    print('No!')
    # esto no se ejecuta
    #print('No!')

print('Adivinaste!')
