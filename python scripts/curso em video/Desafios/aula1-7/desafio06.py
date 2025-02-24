# crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite o seu número: '))
#d = n*2
#t = n*3
#r = n**(1/2) ou pow(n,(1/2))
#print('o dobro do número {} é {}!\n Já o seu triplo é {}!\n Sua raiz quadrada é {}'.format(n, d, t, r))
print('o dobro do número {} é {}!\nJá o seu triplo é {}!\nSua raiz quadrada é {:.2f}'.format(n, (n*2), (n*3), pow(n, (1/2))))
