#Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
n = randint(0, 10)
palpites = 0
print('-=-'*20) #separacao efeito visual
print('voce consegue advinhar o numero escolhido entre 0 e 10?')
print('-=-'*20) #separacao efeito visual
acertou = False
while not acertou:
    jogador = int(input('Qual o seu palpite? '))
    palpites +=1
    if jogador == n:
        acertou = True
    else:
        if jogador < n:
            print('mais...Tente de novo!')
        elif jogador > n:
            print('menos...tente de novo!')
print('Acertou com {} tentativas.'.format(palpites))
