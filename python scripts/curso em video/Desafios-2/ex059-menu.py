from time import sleep
comando = 0
v1 = int(input('Digite um numero: '))
v2 = int(input('Digite outro numero: '))
while comando != 5:
    sleep(1)
    print('-='*20)
    print('>>>>>','''LISTA DE COMANDOS:
        [ 1 ] SOMAR
        [ 2 ] MULTIPLICAR
        [ 3 ] MAIOR
        [ 4 ] NOVOS NUMEROS
        [ 5 ] SAIR DO PROGRAMA ''')
    comando = int(input('Qual comando voce deseja realizar: '))
    print('-='*20)
    if comando == 1:
        soma = v1 + v2
        print('A soma dos valores {} e {} da {}'.format(v1,v2,soma))
    elif comando == 2:
        multi = v1 * v2
        print('A Multiplicacao de {} e {} da {}'.format(v1,v2,multi))
    elif comando == 3:
        if v1 > v2:
            print('O maior numero e o {}'.format(v1))
        elif v2 > v1:
            print('O maior numero e o {}'.format(v2))
        else:
            print('os numeros sao iguais')
    elif comando == 4:
        v1 = int(input('Digite um numero: '))
        v2 = int(input('Digite outro numero: '))
    elif comando > 5:
        print('Informe um comando valido')
print('FIM DO PROGRAMA')