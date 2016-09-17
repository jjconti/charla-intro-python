n = int(input('Tu número: '))

if n > 10:
    print('Ganaste!')
elif n == 5:
    print('Empatamos')
elif n == 9:
    print("Casi")
else:
    print('{0}, gané yo'.format(n + 1))
