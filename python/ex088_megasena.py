from random import randint
from time import sleep

print('-'*30)
print(f'{"JOGO DA MEGA SENA":^30}')
print('-'*30)
jogo = []
qjogos = int(input('Quantos jogos você quer que eu sorteie? '))
print()
for j in range(0, qjogos):
    c = 0
    while c < 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
            c += 1
    jogo.sort()
    print(f'Jogo {j+1}: {jogo}')
    sleep(0.5)
    jogo.clear()
print(f'\n{" < BOA SORTE! > ":-^30}')
