from random import *
from time import *
from operator import *
ranking = list()
cont = 1
jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('Valores sorteados: ')
for k, v in jogo.items():
    sleep(0.5)
    print(f'O jogador {k} jogou {v}')
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('=-=' * 15)
for i, v in enumerate(ranking):
    sleep(0.5)
    print(f'O {i + 1}° lugar foi o {v[0]} com {v[1]}')







