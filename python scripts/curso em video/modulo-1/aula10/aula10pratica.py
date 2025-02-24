n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua media foi {:.1f}'.format(m))
'''if m>= 6:
    print('Parabens voce foi aprovado!')
else:
    print('retido')'''
#ou
print('aprovado'if m >=6.0 else 'retido')