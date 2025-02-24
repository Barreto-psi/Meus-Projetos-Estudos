# par ou impar0
n = int(input('Digite um numero: '))
p = (n%2)
if p == 0:
    print('Seu numero {} e PAR !'.format(n))
else:
    print('Seu numero {} e IMPAR!'.format(n))