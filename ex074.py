from random import randint
cont = 0
numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print('Os números sorteados foram: ', end='')
for n in numeros:
    cont += 1
    print('{} '.format(n), end='')
print('\n')
print(f'O maior foi {max(numeros)}')
print(f'O menor foi {min(numeros)}')

