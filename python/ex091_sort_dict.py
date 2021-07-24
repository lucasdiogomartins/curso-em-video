from random import randint
from time import sleep
from operator import itemgetter

valores = {'jogador1': randint(1, 6),
           'jogador2': randint(1, 6),
           'jogador3': randint(1, 6),
           'jogador4': randint(1, 6)}
# for c in range(1, 5):
#   valores[f'jogador{c}'] = randint(1, 6)

ranking = {}

print('Valores sorteados: ')
for j, v in valores.items():
    print(f'{j} tirou {v} no dado')
    sleep(0.5)
print('=' * 29)
print(' == RANKING DOS JOGADORES == ')
ranking = sorted(valores.items(), key=itemgetter(1), reverse=True)
for p, j in enumerate(ranking):
    print(f'  {p+1}º Lugar: {j[0]} com {j[1]}')
    sleep(0.5)
