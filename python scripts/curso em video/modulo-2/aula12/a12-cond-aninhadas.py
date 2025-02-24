nome = str(input('qual o seu nome? '))
if nome == 'gabriel':
    print('que nome bonito')
elif nome == 'Pedro' or nome == 'paulo':
    print('seu nome e popular no brasil')
elif nome in 'ana claudia juliana':
    print('belo nome feminino')
print('tenha um bom dia, {}'.format(nome))