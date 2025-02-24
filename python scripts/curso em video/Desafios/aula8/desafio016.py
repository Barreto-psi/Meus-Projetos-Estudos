'''#crie um programa que leia um numero real qualquer pelo teclado e mostre na tela a sua porção inteira ex:6.127 parte inteira 6
from math import trunc
num = float(input('Digite um número: '))
real = trunc(num)
print('O número {} tem a parte inteira {} !'.format(num, real))

#print('O número {} tem a parte inteira {} !'.format(num, math.trunc(num)))
#print('O número {} tem a parte inteira {} !'.format(num, trunc(num)))'''

num = float(input('digite um valor:'))
print('o valor digitado foi {} e a sua porção inteira é {}'.format(num, int(num)))
