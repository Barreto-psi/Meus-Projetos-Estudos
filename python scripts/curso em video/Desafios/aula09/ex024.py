#crie um programa que leia o nome de uma cidade e diga se ela comeca ou nao com o nome santo
c = str(input('digite a cidade: ')).strip()
#print('santo'in c.lower()) essa forma se for buscar a palavra independente da posicao
# 
#outra forma
#c = str(input('digite a cidade: ').strip())
print(c[:5].upper == 'SANTO')