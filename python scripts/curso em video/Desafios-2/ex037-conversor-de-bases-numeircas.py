n = int(input('Digite um numero para a conversao: '))
print('''Base de conversao:
1 - para Binario
2 - para octal
3 - para hexadecimal''')
c = int(input('digite o numero referente a base de conversao desejada:'))
if c == 1:
    print('O numero {} em binario e {}!'.format(n, bin(n)[2:]))
elif c == 2:
    print('O numero {} em octal e {}'.format(n,oct(n)[2:]))
elif c == 3:
    print('O numero {} em hexadecimal e {}'.format(n, hex(n)[2:]))
else:
    print('Codigo de conversao invalido')