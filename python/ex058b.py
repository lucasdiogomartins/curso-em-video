from random import randint

computador = randint(1, 11)
print('Pensei em um número de 1 a 10')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é seu palpite?  > '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('Mais... ')
        elif jogador > computador:
            print('Menos... ')
print('acertou em {} tentativas'.format(palpites))
