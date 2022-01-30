pessoas = []
dados = []
maior = menor = 0
r = 'S'
sexo = 'M'
contagem = 1
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(str(input('Digite o peso: ')))
    maior = menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()
    while r[0] not in 'S' or 'N':
        r = str(input('Quer continuar? [S/N] ')).upper()
        if r in 'N':
            teste = False
            break
        if r in 'S':
            dados.append(str(input('Digite o nome: ')))
            dados.append(str(input('Digite o peso: ')))
            if dados[1] > maior:
                    maior = dados[1]
            if dados[1] < menor:
                    menor = dados[1]
            pessoas.append(dados[:])
            dados.clear()
            contagem += 1
    if not teste:
        break

print(f'Foram cadastradas {contagem} pessoas!')
print(f'O(s) maior(es) peso(s) foram de {maior} sendo eles de ', end='')
for aux in pessoas:
    if aux[1] == maior:
        print(f'{aux[0]} ', end='')
print()
print(f'O(s) menor(es) peso(s) foram de {menor} sendo eles de ', end='')
for aux in pessoas:
    if aux[1] == menor:
        print(f'{aux[0]} ', end='')
