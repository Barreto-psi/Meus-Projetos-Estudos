s = 0
cont = 0
for n in range(3, 500, 3):
    if n%2==1:
        cont += 1 # cont = cont + 1
        s += n  # s = s + n
print('a soma dos impares multiplos de tres entre 1 e 500 e {} ao todo foram {} numeros somados'.format(s, cont))
