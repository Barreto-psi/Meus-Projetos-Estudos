#faca um programa que leia uma frase pelo teclado e mostre:
#quantas vezes aparece a letra'A'
#em qual posicao ela aparece a primeira vez
#em qual posicao ela aparece a ultima vez
frase = str(input('Digite a frase: ')).strip().upper()
print('A letra A aparece', frase.count('A'), 'vezes!')
print('A letra A aparece pela primeira vez na posicao de numero: ', frase.upper().find('A')+1)
print('A ultima letra A apareceu na posicao {}'.format(frase.rfind('A')+1))