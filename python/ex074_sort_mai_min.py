from random import randint

valores = (randint(1, 10), randint(1, 10), randint(1, 10),
           randint(1, 10), randint(1, 10), )
print('\nOs valores sorteados foram: ', end='')
for v in valores:
    print(f'{v} ', end='')
print(f'\n\nO maior valor sorteado foi {max(valores)}')
print(f'O menor valor sorteado foi {min(valores)}')
