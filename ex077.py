palavras = ('cubo', 'copo', 'batom', 'oculos', 'jogo', 'lenço', 'caneta', 'planta', 'curso', 'rodrigo')
for p in palavras:
    print(f'\nEm {p.upper()} temos', end='')
    for letra in p:
        if letra in 'aeiou':
            print(letra, end=' ')
