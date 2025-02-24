from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''Suas Opcoes:
[ 0 ] Pedra
[ 1 ] Papel
[ 2 ] Tesoura''')
jo = int(input('Qual e a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-='*11)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[jo]))
print('-='*11)
if pc == 0:
    if jo == 0:
        print('Empatou')
    elif jo == 1:
        print('Voce Ganhou')
    elif jo == 2:
        print('Voce perdeu')
    else:
        print('Jogada invalida')
elif pc == 1:
    if jo == 0:
        print('Voce perdeu')
    elif jo == 1:
        print('Empatou')
    elif jo == 2:
        print('Voce Ganhou')
    else:
        print('Jogada invalida')
elif pc == 2:
    if jo == 0:
        print('Voce ganhou')
    elif jo == 1:
        print('voce perdeu')
    elif jo == 2:
        print('Empatou')
    else:
        print('Jogada invalida')
