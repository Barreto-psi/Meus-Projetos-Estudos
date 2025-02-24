# escreva um programa que leia a velocidade de um carro.
#se ele ultrapassar 80km/h, mostrar uma mensagem dizendo que ele foi multado.
#a multa vai custar R$7,00 por km acima do limite
km = float(input('A quantos km voce estava? '))
if km <= 80:
    print('Pode prosseguir')
else:
    m = (km - 80) * 7
    print('Voce estava acima da velocidade permitida 80km/h!\nSua velocidade foi de {}km/h, voce foi multado em R${:.2f} !'.format(km, m))
