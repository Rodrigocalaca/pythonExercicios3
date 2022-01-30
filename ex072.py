numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
           'seis', 'sete', 'oito', 'nove', 'dez',
           'onze', 'doze', 'treze', 'quatorze', 'quinze',
           'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número: '))
    if n < 0 or n > 20:
        print('Tente novamente.', end='')
        n = int(input('Digite um número: '))
    print('Você digitou o número: {}'.format(numeros[n]))
    aux = str(input('Quer continuar [Sim/Não]: ')).strip().upper()
    if aux[0] == 'N':
        break
print('Fim!')