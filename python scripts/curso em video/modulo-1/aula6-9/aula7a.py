### Ordem de precedencia dos operadores
# 1() 2** 3*,/,//,%  4+,-
n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
#print('A soma vale {}'.format(n1+n2))
    #ou
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
sub = n1 - n2
print('A soma é {}, o produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão inteira {} e potência {}'.format(di,e))
