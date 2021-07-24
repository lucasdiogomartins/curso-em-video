from random import randint
from time import sleep

print('{:=^40}'.format('Jokenpô'))
opt = ('Pedra', 'Papel', 'Tesoura')
comp = randint(0, 2)
print('''
[ 0 ] Pedra 
[ 1 ] Papel
[ 2 ] Tesoura
''')
jog = int(input('Escolha sua jogada => '))

if 0 <= jog <= 2:
    print('JO')
    sleep(0.5)
    print('KEN')
    sleep(0.5)
    print('PÔ')
    sleep(0.5)
    print('-=-'*10)
    print('Jogador: {}'.format(opt[jog]))
    print('Computador: {}'.format(opt[comp]))
    print('-=-'*10, end='\n')
    if jog == comp-1 or jog == comp+2:
        print('Você PERDEU')
    elif jog == comp+1 or jog == comp-2:
        print('Você GANHOU')
    elif jog == comp:
        print('EMPATOU')
    else:
        print('algo deu errado')
else:
    print('Opção inválida')
