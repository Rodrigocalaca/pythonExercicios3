from datetime import *
CLT = ''
dados = dict()
dados['nome'] = str(input('Nome: '))
nascimento = int(input('Ano de nascimento: '))
dados['idade'] = datetime.now().year - nascimento
CLT = str(input('Carteira de trabalho (Caso não tenha deixe o espaço em branco): '))
if CLT != '':
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)
    dados['CLT'] = int(CLT)
for k, v in dados.items():
    print(f'{k}: {v}')


