#pergunte o salario e calculeo valor do seu aumento
#acima de 1.250 aumento de 10%
#abaixo aumento de 15%
s = float(input('Digite seu salário para receber o bonus: R$'))
if s >= 1250:
    b = s + (s*10/100)
    print('Seu salário é de R${:.2f} , com o BONUS de 10% passará a ser R${:.2f} !'.format(s, b))
else:
    b = s + (s*15/100)
    print('Seu salário é de R${:.2f} , com o BONUS de 15% passará a ser R${:.2f} !'.format(s, b))
