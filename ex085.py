valores = [[], []]
aux = 0
for c in range(0, 7):
    aux = int(input('Digite um valor: '))
    if aux % 2 == 0:
        valores[0].append(aux)
    else:
        valores[1].append(aux)
valores[0].sort()
valores[1].sort()
print(valores[0])
print(valores[1])

