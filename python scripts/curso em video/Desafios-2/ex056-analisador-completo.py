#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
s = 0 # soma
mv = 0 # mais velho
qmm = 0 #quantidade mulheres menor 20
for p in range(1, 5):
    nome = str(input('Nome da {}ª pessoa: '.format(p)))
    idade = int(input('Idade da {}ª pessoa: '.format(p)))
    sexo = str(input('Sexo da {}ª pessoa: M, F '.format(p))).upper()
    s += idade
    if sexo == 'F':
        if idade < 20:
            qmm += 1
    elif sexo == 'M':
        homem = nome
        if p == 1:
            mv = idade
        else:
            if idade > mv:
                mv = idade    
    elif sexo != 'M' and sexo !='F':
        print('Informacao invalida')
media = s/4
print('A idade media foi {:.f} anos de idade'.format(media))
print('Homem mais velho se chama {} e tem {} anos'.format(homem,mv))
print('O numero de mulheres abaixo dos 20 anos e {}'.format(qmm))
