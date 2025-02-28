#Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação novamente até ter um valor correto.
sexo = ''
while sexo !='M' and sexo !='F':
    sexo = str(input('sexo [M/F]: ')).strip().upper()
    if sexo == 'M' == 'F':
        print('acabou')