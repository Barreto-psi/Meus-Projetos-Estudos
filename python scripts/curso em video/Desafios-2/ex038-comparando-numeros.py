n1 = int(input('Primeiro numero: '))
n2 = int(input('Segundo numero: '))
if n1 > n2:
    print('O numero {} e maior que {}'.format(n1, n2))
elif n2 > n1:
    print('O numero {} e maior que {}'.format(n2, n1))
else:
    print('Nao existe valor maior, os dois sao iguais')
    