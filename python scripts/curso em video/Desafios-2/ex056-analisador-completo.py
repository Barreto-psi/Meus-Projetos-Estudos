#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
s = 0 # soma
mv = 0 # mais velho
qmm = 0 #quantidade mulheres menor 20
for p in range(1, 5):
    print('-='*5,'{}ª PESSOA'.format(p),'=-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper().strip()
    s += idade
    if sexo == 'F' and idade < 20:
        qmm += 1
    if p == 1 and sexo == 'M':
        homem = nome
        mv = idade
    else:
        if idade > mv:
            mv = idade   
            homem = nome 
    if sexo != 'M' and sexo !='F':
        print('Informacao invalida')
media = s/4
print('A idade media foi {:.1f} anos de idade'.format(media))
print('Homem mais velho se chama {} e tem {} anos'.format(homem,mv))
print('O numero de mulheres abaixo dos 20 anos e {}'.format(qmm))
