import random

secreto = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9])

while int(input('Adiviná: ')) != secreto:
    print('No!')

print('Adivinaste!')
