from random import randint
from time import sleep
n = randint(0, 5)
print('-=-' * 16)
res = int(input('Tente advinhar o número no intervalo de 0 e 5\n > '))
print('Processando...')
sleep(1)
if res == n :
    print('PARABÉNS!')
else:
    print('ERROU!')
print('O número era {}!'.format(n))
print('-=-' * 16)
