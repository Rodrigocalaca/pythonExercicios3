from random import randint

lista = list()
i = int(input('Digite o número inicial do sorteio: '))
f = int(input('Digite o número final do sorteio: '))


def sorteia():
    listaAux = list()
    for c in range(0, 5):
        listaAux.append(randint(i, f))
    return listaAux


def somaPar():
    somatorio = 0
    listaSoma = sorteia()
    for cont in range(0, 5):
        somatorio += listaSoma[cont]
    print(listaSoma)
    print(somatorio)


somaPar()
