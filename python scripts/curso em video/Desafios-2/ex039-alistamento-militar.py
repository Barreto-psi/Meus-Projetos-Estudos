from datetime import date
nascimento = int(input('Ano do seu nascimento: '))
ano = date.today().year
idade = ano - nascimento
print('Quem nasceu em {} tem {} anos em {}.'.format(nascimento, idade, ano))
if idade < 18:
    print('ainda faltam {} anos para o alistamento'.format(18- idade))
elif ano - nascimento > 18:
    print('Voce se alistou em {}'.format(ano-(idade-18)))
else:
    print('VOCE DEVE SE ALISTAR IMEDIATAMENTE!!!')