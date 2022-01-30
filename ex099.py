def maiorValor(lista):
    cont = 0
    maior = 0
    for valor in lista:
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(maior)


numeros = list()
quantidade = int(input('Digite quantos números quer testar: '))
for c in range(0, quantidade):
    numeros.append(int(input(f'Numero {c + 1}:')))


maiorValor(numeros)

