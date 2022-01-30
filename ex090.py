dados = dict()
dados['nome'] = str(input('Digite o nome do aluno: '))
dados['média'] = float(input('Digite a média do aluno: '))
if dados['média'] >= 7:
    dados['situação'] = 'aprovado'
elif 6 <= dados['média'] < 7:
    dados['situação'] = 'reforço'
else:
    dados['situação'] = 'reprovado'
for k, v in dados.items():
    print(f'{k} = {v}')


