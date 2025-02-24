#testes 
n = 'Gabriel'
#dicionario entre {}
cores = {'limpa':'\033[m',
         'azul':'\033[34m', 
         'amarelo':'\033[33m'}

print('Ola {}{}{}!!!'.format(cores['amarelo'], n, cores['limpa']))
#print('Ola {}{}{}!!!'.format('\033[4;31m', n, '\033[m'))
