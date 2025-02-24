#pergunte a distancia de uma viagem em Km.
#calcule o preco da passagem, cobrando RS0.50 por Km para viagens ate 200km
# e RS0.45 para viagens maiores
d = float(input('Quantos Km de distancia tem a viagem? '))
if d <= 200:
    print('O Valor da viagem de {:.0f}Km sera de R${:.2f} !'.format(d, (d*0.5)))
else:
    print('O Valor da viagem de {:.0f}Km sera de R${:.2f} !'.format(d, (d*0.45)))
