from random import randint

num = randint(1, 10)
print('Pensei em um número de 1 à 10, será que adivinhas?')
palp = int(input(' >> '))
tent = 1
while palp != num:
    if num > palp:
        palp = int(input('Mais... \n >> '))
    elif num < palp:
        palp = int(input('Menos... \n >> '))
    tent += 1
print('Adivinhou em {} tentativas'.format(tent))
