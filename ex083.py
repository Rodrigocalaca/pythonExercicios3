abrindo = 0
fechando = 0
termos = str(input('Digite a expressão: '))
for c in termos:
    if c == '(':
        abrindo += 1
    if c == ')':
        fechando += 1
if abrindo == fechando:
    print('Expressão válida!')
else:
    print('Expressão inválida!')