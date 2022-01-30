matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
tam = 3
somapar = 0
somaterceiracoluna = 0
maiorvalorsegundalinha = 0
for l in range(0, tam):
    for c in range(0, tam):
        matriz[l][c] = int(input(f'Digite o valor {l + 1}, {c + 1}: '))
for l in range(0, tam):
    for c in range(0, tam):
        print(f'{matriz[l][c]:^5}', end='')
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if l == 1:
            if c == 0:
                maiorvalorsegundalinha = matriz[l][c]
            if c == 1:
                if matriz[l][c] > maiorvalorsegundalinha:
                    maiorvalorsegundalinha = matriz[l][c]
            if c == 2:
                if matriz[l][c] > maiorvalorsegundalinha:
                    maiorvalorsegundalinha = matriz[l][c]
    print()
print('-='*30)
print(somapar)
for l in range(0, tam):
    somaterceiracoluna += matriz[l][2]
print(somaterceiracoluna)
print(maiorvalorsegundalinha)
print('-='*30)
