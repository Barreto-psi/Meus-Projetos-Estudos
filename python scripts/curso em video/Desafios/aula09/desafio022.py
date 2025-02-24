#crie um programa que leia o nome completo de uma pessoa
# o nome com todas as letras maiusculas
# o nome com todas as letras minusculas
#quantas letras ao todo (sem considerar espacos)
#quantas letras tem o primeiro nome
nome = str(input('Digite seu nome inteiro: ')).strip()
#nome = 'Gabriel Barreto Haran'
print(nome.upper())
print(nome.lower())
#lc = len(nome) #numero de letras totais
#ce = nome.count(' ', 0, lc) #numero de espacos entre os nomes
#letras = int(lc-ce) 
print('O seu nome tem {} Letras.'.format(len(nome) - nome.count(' ')))
print('O seu primeiro nome tem {} letras!'.format(nome.find(' ')))
#nome = nome.split()
#print('O seu primeiro nome {}, tem {} letras.'.format(nome[0], len(nome[0])))

