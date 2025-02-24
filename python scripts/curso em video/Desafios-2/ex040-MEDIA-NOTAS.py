n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2
print('Tirando {:.1f} e {:.1f} a media do aluno e {:.1f}'.format(n1, n2, media))
if media < 5.0:
    print('REPROVADO')
elif media > 7:
    print('APROVADO')
else:
    print('RECUPERACAO')
# 
# outro
#if media >=5 and media < 7:
#   print('RECUPERACAO')