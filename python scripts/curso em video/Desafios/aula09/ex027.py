# ultima palavras com len -1
nome = str(input('Escreva seu nome: ')).strip().upper()
pnome = nome.split()
print('Olá, {}!\n Seu primeiro nome e {}\n Seu ultimo nome e {}'.format(nome, pnome[0], pnome[len(pnome)-1]))