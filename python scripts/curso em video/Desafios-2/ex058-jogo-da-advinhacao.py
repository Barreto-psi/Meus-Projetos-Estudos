#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep
n = randint(0, 10)
cont = 0
print('-=-'*20) #separacao efeito visual
u = int(input('Adivinhe o numero escolhido entre 0 e 10: '))
print('-=-'*20) #separacao efeito visual
print('PROCESSANDO...')
sleep(1)
while u != n:
    if u > n:
        u = int(input('Menos...Tente de novo: '))
    elif u < n:
        u = int(input('Mais...Tente de novo: '))
    cont += 1
    print('PROCESSANDO...')
    sleep(1)
if u == n:
    print('Parabens voce acertou o numero escolhido foi {} !\nSo foram necessarios {} palpites'.format(n,cont+1))
