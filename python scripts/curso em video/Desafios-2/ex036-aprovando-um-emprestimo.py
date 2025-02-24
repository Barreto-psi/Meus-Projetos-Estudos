#o programa vai perguntar o valor da casa, o salario do comprador e em quantos anos vai pagar
#calcule o valor da prestacao sabendo que 
# ela nao pode exercer 30% do salario ou entao o emprestimo sera negado
casa = float(input('Qual o valor da casa desejada? R$'))
salario = float(input('Qual o seu salario? R$'))
tempo = float(input('em quantos anos voce pretende quitar a casa? '))
prest = casa/(tempo* 12)
if prest > (salario*30/100):
    print('Emprestimo negado por exceder 30% ', 'do salario!', end='')
    print(' Sua parcela seria de R${:.2f} por mes'.format(prest))
else:
    print('Emprestimo aprovado', end='')
    print('Sua parcela sera de R${:.2f} por mes durante o periodo de {:.0f} anos!'.format(prest,tempo))