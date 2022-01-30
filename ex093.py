dados = dict()
gols = list()
total = 0
dados['nome'] = str(input('Nome do jogador: '))
quant = int(input('Quantas partidas ele jogou: '))
for c in range(0, quant):
    gols.append(int(input(f'\tQuantos gols na partida {c + 1}: ')))
    total += gols[c]
dados['gols'] = gols
dados['total'] = total
print('=~' * 20)
for k, v in dados.items():

    print(f'{k}: {v}')
print('=~' * 20)
print(f'O jogador {dados["nome"]} jogou {quant} partidas')
for cont in range(0, quant):
    print(f'\t=> Na partida {cont + 1}, fez {gols[cont]} gols')
print(f'No total foram {dados["total"]} gols')
print('=~' * 20)



