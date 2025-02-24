produto = float(input('Valor do produto: R$'))
print('''Formas de pagamento:
    1 - A vista/cheque: desconto 10%
    2 - A vista no Cartao: desconto 5% 
    3 - 2x no cartao: Preco normal
    4 - 3x ou mais no cartao: juros de 20% ''')
opcao = int(input('Qual numero acima refere a sua opcao de pagamento? '))
if opcao == 1:
    print('Com o desconto de 10%, seu produto custara R${:.2f}'.format(produto - (produto*10/100)))
elif opcao == 2:
    print('Com o desconto de 5%, seu produto custara R${:.2f}'.format(produto - (produto*5/100)))
elif opcao == 3:
    print('O Valor do seu produto e R${:.2f} e cada parcela saira a R${:.2f}'.format(produto, produto / 2))
elif opcao == 4:
    print('Com os juros de 20%, seu produto custara R${:.2f}'.format(produto + (produto*20/100)))
else:
    print('Forma de pagamento invalida. Tente novamente')