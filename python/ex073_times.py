times = ('Flamengo', 'Palmeiras', 'Corinthians', 'Atlético-GO', 'São Paulo',
         'Fluminense', 'Atlético-MG', 'Fortaleza', 'Internacional', 'Sport',
         'Ceará', 'Grêmio', 'Bahia', 'Santos', 'Chapecoense', 'Bragantino',
         'Athletico-PR', 'América-MG', 'Cuiabá', 'Juventude')
print('-=-' * 20)
print(f'Lista de Times: {times}')
print('-=-' * 20)
print(f'Os 5 primeiros são: {times[0:5]}')
print('-=-' * 20)
print(f'Os últimos 4 colocados são: {times[-4:]}')
print('-=-' * 20)
print(f'Times em Ordem alfabética {sorted(times)}')
print('-=-' * 20)
print(f'O Chapecoense está na {times.index("Chapecoense") + 1}° posição')
print('-=' * 30)