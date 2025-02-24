#escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. calcule o preco a pagar, sabendo que o carro custa 60,00 o dua e ,15 por km rodado
d = float(input('Por quantos dias foi alugado? '))
km = float(input('Quantos km foram percorridos durante o aluguel? '))
p = ((d * 60) + (km * 0.15))
print('O valor a ser pago é de R${:.2f} !'.format(p))
