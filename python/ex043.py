peso = float(input('Qual é seu peso (kg) '))
altura = float(input('Qual é sua altura? (m) '))
imc = peso / altura ** 2
print('O imc dessa pessoa é de {:.1f}, está '.format(imc), end='')
if imc < 18.5:
    print('MAGRELO')
elif imc < 25:
    print('no PESO IDEAL')
elif imc < 30:
    print('em SOBREPESO')
elif imc < 40:
    print('OBESO, cuidado!')
else:
    print('em OBESIDADE MÓRBIDA, cuidado!')
