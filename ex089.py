lista = list()
alunos = list()
continuar = 'S'
while True:
    lista.append(str(input('Nome do aluno: ')))
    nota1 = float(input('Primeira nota do aluno: '))
    nota2 = float(input('Segunda nota do aluno: '))
    notas = [nota1, nota2]
    lista.append(notas)
    media = (nota1 + nota2)/2
    lista.append(media)
    alunos.append(lista[:])
    lista.clear()
    while continuar[0] not in 'S' or 'N':
        continuar = str(input('Quer continuar? [S/N] ')).upper()
        if continuar[0] in 'S':
            lista.append(str(input('Nome do aluno: ')))
            nota1 = float(input('Primeira nota do aluno: '))
            nota2 = float(input('Segunda nota do aluno: '))
            notas = [nota1, nota2]
            lista.append(notas)
            media = (nota1 + nota2) / 2
            lista.append(media)
            alunos.append(lista[:])
            lista.clear()
        if continuar[0] in 'N':
            teste = False
            break
    if not teste:
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 30)
for i, a in enumerate(alunos):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
aux = 'S'
print('-=' * 30)
while True:
    indice = int(input('Digite o número correspondente do aluno para ver as notas: '))
    if indice <= len(alunos) - 1:
        print(f'Notas de {alunos[indice][0]} são {alunos[indice][1]}')
    while aux[0] not in 'S' or 'N':
        aux = str(input('Fazer outra verificação? [S/N] ')).upper()
        if aux[0] == 'N':
            teste2 = False
            break
        if aux[0] == 'S':
            indice = int(input('Digite o número correspondente do aluno para ver as notas: '))
            if indice <= len(alunos) - 1:
                print(f'Notas de {alunos[indice][0]} são {alunos[indice][1]}')
    if not teste2:
        break
print('FIM')


