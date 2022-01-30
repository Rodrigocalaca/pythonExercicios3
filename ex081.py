cont = 0
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    r = str(input('Quer continuar? [S/N]: ')).upper()
    cont += 1
    if r[0] == 'N':
        break
print(f'foram digitados {cont} valores')
valores.sort(reverse=True)
print(f'Os valores de forma decressente são {valores}')
if 5 in valores:
    print('O valor 5 está na lista!')
else:
    print('O valor 5 não está na lista!')
