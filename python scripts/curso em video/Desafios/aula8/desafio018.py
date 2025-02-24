#faça um programa que leia um angulo qualquer e mostre na tela o falor do seno, cosseno e tangente desse angulo
'''import math
ang = float(input('Digite o Ângulo: '))
rad = math.radians(ang)
seno = math.sin(rad)
cosseno = math.cos(rad)
tangente = math.tan(rad)
print('A partir do angulo {:.3f} o seno é {:.3f}, o cosseno é {:.3f} e a tangente é {:.3f}!'.format(ang, seno, cosseno, tangente))'''

#reduzindo o codigo
from math import radians, sin, cos, tan
ang = float(input('Angulo:'))
print('Para o angulo {}, o seno é {:.2f} o cosseno é {:.2f} e a tangente é {:.23f} !'.format(ang, (sin(radians(ang))), (cos(radians(ang))), tan(radians(ang))))
