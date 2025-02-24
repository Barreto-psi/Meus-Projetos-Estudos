# escreva um programa que faca o computador "pensar" em um numero inteiro entre 0 e 5 
# e peca para o usuario tentar definir qual foi o numero escolhido pelo computador.
#o programa devera escrever na tela se o usuario venceu ou perdeu.
from random import randint
from time import sleep
n = randint(0, 5)
print('-=-'*20) #separacao efeito visual
u = int(input('Adivinhe o numero escolhido entre 0 e 5: '))
print('-=-'*20) #separacao efeito visual
print('PROCESSANDO...')
sleep(2)
if u == n:
    print('Parabens voce acertou o numero escolhido foi {} !'.format(n))
else:
    print('Voce errou! O numero escolhido foi {} e voce chutou {}...'.format(n, u))
