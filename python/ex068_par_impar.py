from random import randint

win = 0
print('-=-'*10)
print('Vamos Jogar PAR OU IMPAR')
print('-=-'*10)
# Loop de Jogo
while True:
    player = -1
    while True:
        player = int(input('Diga um valor: '))
        if player in range(0, 11):
            break
        else:
            print(f'Você não tem {player} dedos!')
    computer = randint(0, 10)
    result = player + computer
    choice = ' '
    while choice not in 'PI':
        choice = input('PAR ou IMPAR? [P/I] >').strip().upper()[0]
    # Mostrar dados no console
    print('-' * 30)
    print(f'Você jogou {player} e o computador jogou {computer}. Total de {result}. ', end='')
    print('Deu PAR' if result % 2 == 0 else 'Deu ÍMPAR')
    # Verificar se ganhou ou perdeu
    if result % 2 == 0:
        if choice == 'P':
            print('VOCÊ VENCEU')
            win += 1
        else:
            print('VOCÊ PERDEU')
            break
    elif result % 2 != 0:
        if choice == 'I':
            print('VOCÊ VENCEU')
            win += 1
        else:
            print('VOCÊ PERDEU')
            break
    print('Vamos Jogar novamente...')
    print('-=-'*15)
    # volta para Loop de Jogo
print('-=-'*15)
print(f'GAME OVER! Você venceu {win} vezes')
