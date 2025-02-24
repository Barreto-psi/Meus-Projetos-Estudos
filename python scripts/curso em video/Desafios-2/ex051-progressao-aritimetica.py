termo = int(input('Primeiro termo: '))
razao = int(input('razao: '))
#
#  s = termo - razao
# for c in range(1,11): #repetir 10x
#     pa = termo + razao
#     s += pa
#     print(s, end='-')
# print('FIM')
#ou
decimo = termo + (10 - 1)* razao
for c in range(termo, decimo + razao, razao):
    print('{}'.format(c), end='-')
print('FIM')
