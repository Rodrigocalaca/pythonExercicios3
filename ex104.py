def leiaInt(num):
    validacao = False
    valor = 0
    while True:
        n = str(input(num))
        if n.isnumeric():
            check = isinstance(n, float)
            if check:
                print('\033[0;31mINSIRA UM NÚMERO INTEIRO\033[m')
            else:
                valor = int(n)
                validacao = True
            break
        else:
            print('\033[0;31mINSIRA UM NÚMERO INTEIRO\033[m')
        if validacao:
            break
    return valor


teste = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {teste}')


