#manipulando cadeia de textos
frase = 'Curso em Video python'
#           FATIAMENTO  
# #print(frase[9:13]) # Vide  #vai do 9 ao 12 o 13 n conta, sempre uma a menos no final
#print(frase[9:21:2]) # Vdeopto vai pulando 2 caracteres
#print(frase[:5]) #cruso #começa do inicio ate o numero
#print(frase[15:]) #python # do caractere ao final
#print(frase[9::3]) #Veph #começa no nove vai ate o final e pulando 3
#
#           ANÁLISE
len(frase)
frase.count('o', 0, 13 ) #contar quantas vezes aparece a letra maiuscula ou minuscula 
#                               de acordo com o range colocado 0 a 12 ja que o 13 n conta
frase.find('deo') #mostra onde iniciou posicao 11
frase.find('Android') #mostra -1 porque n possui esse trecho na frase, 
#                      sempre que aparecer o -1 e por nao existe o q esta procurando
'Curso'in frase # = resposta true #indica se existe ou n a palavra dentro da frase
#
#           TRANSFORMAÇÃO
frase.replace('python', 'Android') # trocar uma palavra do texto por outra de fora
frase.upper() #ficar em maiusculo
frase.lower() #ficar em minusculo
frase.capitalize() #todos os caracteres pra minusculos e so a primeira letra ficara em maiuscula
frase.title() #a primeira letra de todas as palavras do range em maiusculo
###
#frase = '   Aprenda Python  '
frase.strip() #remove espacos inuteis do comeco e do fim da string 
#              sendo a primeira letra numa nova contagem valendo 0
frase.rstrip() #remove so o lado direito ou seja os espacos finais
frase.lstrip() #remove o lado esquerdo ou seja espacos iniciais
#
#           DIVISÃO
frase.split() #cria uma divisao nos espacos. 
#ou seja cada palavra recebe indexacao numerica nova, sempre comecando do 0
#cria uma lista com todas as palavras de uma cadeia de caracteres
#           JUNÇÃO
'-'.join(frase) #junta as frases com o caractere entre as aspas
#ex: curso-em-video-python