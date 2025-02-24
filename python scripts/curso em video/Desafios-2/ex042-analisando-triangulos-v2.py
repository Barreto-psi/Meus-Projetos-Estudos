a = float(input('Digite a primeira reta: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))
if a < b + c and b < a + c and c < b + a:
    print('com as medidas {}, {} e {}, podemos formar um triangulo!'.format(a, b, c))
    if a == b == c:  # ou a == b and b == c:
        print('Este triangulo e EQUILATERIO')
    elif a == b and b != c or b == c and b != a or a == c and c != b:
        print('Este triangulo e ISOSCELES')
    else:
        print('Este triangulo e ESCALENO') 
else:
    print('nao e possivel formar um triangulo com as retas {}, {} e {}'.format(a, b, c))
