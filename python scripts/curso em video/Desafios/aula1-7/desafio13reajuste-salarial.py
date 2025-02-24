#faça um algoritimo que leia o salario de um funcionário e mostra seu novo salario, com 15% de aumento
s = float(input('Digite seu salário para receber o bonus: R$'))
b = s + (s*15/100)
print('Seu salário é de R${:.2f} , com o BONUS de 15% passará a ser R${:.2f} !'.format(s, b))
