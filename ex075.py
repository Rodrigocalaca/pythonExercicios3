par = 0
impar = 0
valores = tuple(int(input('Digite valores: '))for c in range(0, 5))
print('Você digitou o valor 9, {} vezes'.format(valores.count(9)))
if 3 in valores:
    print('A posição do primeiro valor 3 é: {}°'.format(valores.index(3) + 1))
else:
    print('Não foi digitado nenhum valor 3')
print('Os valores pares digitados foram: ', end='')
for cont in range(len(valores)):
    if valores[cont] % 2 == 0:
        par = valores[cont]
        print(f'{par},', end=' ')
    else:
        impar += 1
    if impar == len(valores):
        print('Nenhum valor par foi digitado')







