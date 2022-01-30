dados = dict()
gols = list()
time = list()
total = 0
resposta = 'S'
while True:
    dados.clear()
    dados['nome'] = str(input('Nome do jogador: '))
    quant = int(input('Quantas partidas ele jogou: '))
    for c in range(0, quant):
        gols.append(int(input(f'\tQuantos gols na partida {c + 1}: ')))
        total += gols[c]
    dados['gols'] = gols
    dados['total'] = total
    time.append(dados.copy)
    while resposta not in 'N' or 'S':
        resposta = str(input('Quer continuar [S/N]: ')).upper()
        if resposta[0] == 'S':
            dados.clear()
            dados['nome'] = str(input('Nome do jogador: '))
            quant = int(input('Quantas partidas ele jogou: '))
            for c in range(0, quant):
                gols.append(int(input(f'\tQuantos gols na partida {c + 1}: ')))
                total += gols[c]
            dados['gols'] = gols
            dados['total'] = total
            time.append(dados.copy)
        if resposta[0] == 'N':
            teste = False
            break
    if not teste:
        break
print('-' * 40)
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)
