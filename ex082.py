valores = []
pares = []
impares = []
r = 'S'
while True:
    valores.append(int(input('Digite um valor: ')))
    while r[0] not in 'S' or 'N':
        r = str(input('Quer continuar? [S/N]: ')).upper()
        if r[0] in 'N':
            teste = False
            break
        elif r[0] in 'S':
            valores.append(int(input('Digite um valor: ')))
    if not teste:
        break
print(f'A lista original são os valores {valores}')
for i, v in enumerate(valores):
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 != 0:
        impares.append(v)
print(f'Os valores pares são: {pares}')
print(f'Os valores pares são: {impares}')

