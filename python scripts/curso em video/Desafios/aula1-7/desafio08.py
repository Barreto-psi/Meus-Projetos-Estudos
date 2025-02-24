#escreva um programa que leia um valor em metros e o exima convertido em centímetros e milimetros. 1m == 100 cm
m = float(input('Digite a medida: '))
cm = m / 0.01 # m*100
mm = m / 0.001 # m*1000
print('{}m = {:.0f}cm ou {:.0f}mm !'.format(m, cm, mm))