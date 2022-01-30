valores = list()
cont = 1
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado')
    respostas = str(input('Quer continuar? [S/N]: ')).upper()
    if respostas[0] == 'N':
        break
    cont += 1
valores.sort()
print(valores)
