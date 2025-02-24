#faça um algoritimo que leia o preço de um produto e mostre o seu novo preço, com 5% de desconto
p = float(input('Digite o preço para obter o desconto:'))
d = p*5/100
print('Seu preço com o desconto de 5% será {:.2f}! Você economisou {:.2f}!'.format((p-d), d))
      