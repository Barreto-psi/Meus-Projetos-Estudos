#leia o comprimento  de tres retas e diga ao usuario se elas podem ou nao formar um triangulo
a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))
'''if a < b + c:
    if b < a + c:
        if c < b + a:
            print('com as medidas {},{} e {}, podemos formar um triangulo!'.format(a, b, c))
        else:
            print('nao e possivel formar um triangulo com as retas {}, {} e {}'.format(a, b, c))
    else:
        print('nao e possivel formar um triangulo com as retas {}, {} e {}'.format(a, b, c))
else:
    print('nao e possivel formar um triangulo com as retas {}, {} e {}'.format(a, b, c))'''
if a < b + c and b < a + c and c < b + a:
    print('com as medidas {},{} e {}, podemos formar um triangulo!'.format(a, b, c))
else:
    print('nao e possivel formar um triangulo com as retas {}, {} e {}'.format(a, b, c))