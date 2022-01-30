def ficha():
    nome = str(input('Digite o nome do jogador: '))
    gols = str(input('Digite quantos gols o jogador fez: '))
    if nome == '':
        nome = 'Desconhecido'
    if gols.isnumeric():
        gols = int(gols)
    else:
        gols = 0
    if gols == '':
        gols = 0
    print(f'O jogador {nome} fez {gols} gol(s)')


ficha()


