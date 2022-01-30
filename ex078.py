valores = []
posmaior = 0
posmenor = 0
for c in range(0, 5):
    valores.append(int(input(f'valor na posição {c + 1}: ')))
    if c == 0:
        maior = menor = valores[c]
    if valores[c] > maior:
        maior = valores[c]
    if valores[c] < menor:
        menor = valores[c]
for cont in range(0, 5):
    print(f'{valores[cont]} ', end='')
print()
for i, v in enumerate(valores):
    if v == maior:
        posmaior = i
for i, v in enumerate(valores):
    if v == menor:
        posmenor = i
print(f'O maior foi número foi {maior} e foi encontrado na posição {posmaior}')
print(f'O menor foi número foi {menor} e foi encontrado na posição {posmenor}')

