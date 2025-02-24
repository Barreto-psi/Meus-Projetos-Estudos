#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pintala. sabendo que cada litro equivale a uma area de 2m²
l = float(input('Digite a largura: '))
al = float(input('Digite a altura: '))
a = l*al
t = a/2
print('Com Largura {:.2f}m e Altura de {:.2f}m, a área a ser pintada sera de {:.2f}m²'.format(l, al, a))
print('Você precisará para pintar a área de {:.2f}m², {:.2f}L de tinta!'.format(a, t))