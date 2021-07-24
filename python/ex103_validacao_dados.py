def mostrar(n='', g=''):
    if n == '':
        n = '<desconhecido>'
    if not g.isnumeric():
        g = 0
    return f'O jogador {n} fez {g} gol(s) no campeonato'


# Main
nome = input('Nome do Jogador: ').title()
gols = input('Número de Gols: ')
print(mostrar(nome, gols))
