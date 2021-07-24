jogador = dict()
gols = list()
jogador['nome'] = input('Nome do jogador: ').strip().title()
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

for p in range(0, partidas):
    gols.append(int(input(f'Quantos gols na partida {p+1}? ')))
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('=' * 60)
print(jogador)
print('=-' * 25)

for k, v in jogador.items():
    print(f'O campo "{k}" tem o valor: {v}')
print('=-' * 25)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for p, g in enumerate(jogador['gols']):
    print(f'    => Na partida {p+1}, fez {g} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
