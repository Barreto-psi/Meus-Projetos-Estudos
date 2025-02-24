#escrevva um programa que converta uma temperatura digitada em c° e converta para f°  formula da conversão F = C x 9 / 5 + 32
c = float(input('Qual a temperatura em C° :'))
f = ((c * 9) / 5) + 32
print('A temperatura {:.2f}C° sera equivalente a {:.2f}F° !'.format(c, f))
