#sorteio 4 alunos escrevendo o nome deles e escrefendo o nome escolhido
from random import choice
n1 = input('Aluno 1: ')
n2 = input('Aluno 2: ')
n3 = input('Aluno 3: ')
n4 = input('Aluno 4: ')
lista = [n1, n2, n3, n4]
es = choice(lista)
print('O nome Sorteado é: {}'.format(es))