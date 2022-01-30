matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tam = 3
for l in range(0, tam):
    for c in range(0, tam):
        matriz[l][c] = int(input(f'Digite o valor {l + 1}, {c + 1}: '))
for l in range(0, tam):
    for c in range(0, tam):
        print(f'{matriz[l][c]:^5}', end='')
    print()

