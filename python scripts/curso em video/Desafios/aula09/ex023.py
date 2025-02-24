#faca um programa que leia um numero de a 9999 e 
# mostre na tela cada um dos seus digitos separados: unidade, dezena, sentena, milhar
num = int(input('Digite um numero entre 0 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num //1000 % 10
print('Unidade: ', u)
print('Dezena:  ', d)
print('Centena: ', c)
print('Milhar:  {}'.format(m))
