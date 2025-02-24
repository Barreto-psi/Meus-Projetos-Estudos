frase = str(input('Digite a frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1] # solucao em fatiamento
#solucao em for
'''inverso = '' 
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]'''

if inverso == junto:
    print('E Palindromo')
else:
    print('NAO e Palindromo')
print(inverso)