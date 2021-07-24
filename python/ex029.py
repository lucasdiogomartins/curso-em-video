vel = int(input('Velocidade do carro em km/h: '))
if vel > 80:
    print('MULTADO! Você ultrapassou o limite permitido de 80km/h')
    mul = 7 * (vel-80)
    print('Deverá pagar R${:.2f} de multa'.format(mul))
print('Tenha um bom dia! Dirija com segurança')
