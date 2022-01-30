from datetime import date
dataAtual = date.today().year


def voto(ano):
    if dataAtual - ano > 18:
        print('Voto obrigatório')
    elif 18 >dataAtual - ano > 16:
        print('Voto opicional')
    else:
        print('Voto negado')


x = int(input('Digite o ano de nascimento pra consulta: '))
voto(x)


