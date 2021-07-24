time = list()
jogador = dict()
gols = list()

while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = input('Nome do jogador: ').strip().title()
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for p in range(0, partidas):
        gols.append(int(input(f'Quantos gols na partida {p+1}? ')))

    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    while True:
        resp = input('Quer continuar? [S/N] ').upper()[0]
        if resp in 'SN':
            break
        print(' * ERRO: Digite apenas S ou N!')
    if resp == "N":
        break

print('='*48)
print(f'cod  ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-'*42)
for c, j in enumerate(time):
    print(f'{c:>3}  ', end='')
    for d in j.values():
        print(f'{str(d):<15}', end='')  # str() para formatar listas
    print()
print('='*48)

while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time):
        print(f' * ERRO: Não existe jogador com código {busca}')
    else:
        print(f' -- Levantamento do Jogador {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    no jogo {i+1} fez {g} gols')
    print('-'*48)
print('<< VOLTE SEMPRE >>')
