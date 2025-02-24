#faca um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo retangulo , calcule e mostre o comprimento da himpotenuza
from math import pow, sqrt, hypot
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
h = sqrt(pow(co, 2) + pow(ca, 2))
print('Se o comprimento do cateto oposto for {} e do cateto adjacente for {}, o valor da hipotenuza sera {:.3f} !'.format(co, ca, h))

#import math ----   hi = math.hypot(co, ca) 
#       ou 
# from math import hypot -------- h = hypot(co, ca)