lista = ('Lápis', 1.5, 'Caneta', 2.0, 'Borracha', 1, 'estojo', 10.00, 'Régua', 5)
print('-='*20)
for c in range(0, len(lista)):
    if c % 2 == 0:
        print(f'{lista[c]:.<30}', end=' ')
    else:
        print(f'R${lista[c]:>.2f}')
print('-='*20)