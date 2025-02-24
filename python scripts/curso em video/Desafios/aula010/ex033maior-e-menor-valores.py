#faca um programa que leia 3 numeros e mostre qual o maior e o menor
n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('digite o terceiro numero: '))
#primeiro forma que encontrei
'''if n1 > n2:
    if n1 > n3:
        if n2 > n3:
            print('Maior numero {} e o menor {}'.format(n1, n3))
        else:
            print('Maior numero {} e o menor {}'.format(n1, n2))
    else:
        print('Maior numero {} e o menor {}'.format(n3, n1))
else:
    if n2 > n3:
        if n3 > n1:
            print('Maior numero {} e o menor {}'.format(n2, n1))
        else:
            print('Maior numero {} e o menor {}'.format(n2, n3))
    else:
        print('Maior numero {} e o menor {}'.format(n3, n1))'''
#verificando quem e menor
me = n1
if n2 < n1 and n2 < n3:
    me = n2
if n3 < n1 and n3 < n2:
    me = n3
#verificando o maior
ma = n1
if n2 > n1 and n2 > n3:
    ma = n2
if n3 > n1 and n3 > n2:
    ma = n3
print('o Numero maior e {}\n O numero menor e {}'.format(ma, me))
