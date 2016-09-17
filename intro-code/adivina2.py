import random

secreto = random.choice(range(1, 100))

while int(input('Adiviná (1-100): ')) != secreto:
    print('No!')

print('Adivinaste!')
