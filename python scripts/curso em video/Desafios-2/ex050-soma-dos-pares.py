s = 0
cont = 0
for c in range(1, 7):
    n = int(input('Escreva o {} numero inteiro: '.format(c)))
    if n%2 == 0:
        s += n
        cont += 1
print('voce informou {} numeros pares e a soma deles deu {}'.format(cont,s))
