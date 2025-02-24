from datetime import date
ano = date.today().year
cont = 0
for pessoas in range(1,8):
    data = int(input('Em que ano a {}ª pessoa nasceu: '.format(pessoas)))
    idade = ano - data
    if idade >= 18:
        cont += 1
print('Ao todo tivemos {} pessoas maiores de idade,'.format(cont))
print('E tambem tivemos {} pessoas menores de idade.'.format(7 - cont))