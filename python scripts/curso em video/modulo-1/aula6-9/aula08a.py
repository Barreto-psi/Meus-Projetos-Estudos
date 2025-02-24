#trabalhando Modulos ---- para incluir algo comando 'import'
###Biblioteca inteira
import math
num = int(input('digite um numero: '))
raiz =  math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
#print('A raiz de {} é igual a {}'.format(num, ceil(raiz))) #arredondamento


### somente a funcionalidade da biblioteca
from math import sqrt
#from math import sqrt, floor = duas funcionalidades a raiz e o arredondamento pra baixo
num = int(input('digite um numero: '))
raiz = sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
