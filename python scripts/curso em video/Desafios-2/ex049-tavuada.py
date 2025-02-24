n = int(input('Escolha um numero para ver a tabuada: '))
for t in range(0, 11):
    print('{} X {:2} = {}'.format(n, t, n*t))
