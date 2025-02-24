altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))
imc = peso / pow(altura, 2)
print('Seu IMC e {:.2F} e seu status e: '.format(imc), end='')
if imc < 18.5:
    print('Abaixo do Peso')
elif 25> imc >= 18.5:
    print('Peso Ideal')
elif imc < 30:
    print('SOBREPESO')
elif 40 > imc >= 30:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')