pessoa = dict()
cadastros = list()
continuar = 'S'
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    sexo = str(input('Gênero [Masculino/Feminino]: ')).upper().strip()
    if sexo != 'MASCULINO' and sexo != 'FEMININO':
        print('Erro! digite novamente.')
        sexo = str(input('Gênero [Masculino/Feminino]: ')).upper().strip()
    else:
        pessoa['sexo'] = sexo
    idade = int(input('Idade: '))
    if idade < 0:
        print('Erro! digite novamente.')
        idade = int(input('Idade: '))
    else:
        pessoa['idade'] = idade
        soma += pessoa['idade']
    cadastros.append(pessoa.copy())
    while continuar[0] not in 'S' or 'N':
        continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()
        if continuar[0] in 'S':
            pessoa['nome'] = str(input('Nome: '))
            sexo = str(input('Gênero [Masculino/Feminino]: ')).upper().strip()
            if sexo != 'MASCULINO' and sexo != 'FEMININO':
                print('Erro! digite novamente.')
                sexo = str(input('Gênero [Masculino/Feminino]: ')).upper().strip()
            else:
                pessoa['sexo'] = sexo
            idade = int(input('Idade: '))
            if idade < 0:
                print('Erro! digite novamente.')
                idade = int(input('Idade: '))
            else:
                pessoa['idade'] = idade
                soma += pessoa['idade']
            cadastros.append(pessoa.copy())
        if continuar[0] in 'N':
            teste = False
            break
    if not teste:
        break
print('~=' * 20)
# quantas pessoas foram cadastradas
print(f'Foram cadastradas {len(cadastros)} pessoas')
# média de idade
media = soma/len(cadastros)
print(f'A média de idade é {media} anos')
# lista de mulheres
print('As mulheres cadastradas foram: ')
for p in cadastros:
    if p['sexo'] in 'FEMININO':
        print(f'{p["nome"]} ', end=';')
print()
# lista de pessoas com idade acima da média
print('As pessoas com idade acima da média foram: ')
for p in cadastros:
    if p['idade'] >= media:
        print(f'{p["nome"]} ', end=';')
