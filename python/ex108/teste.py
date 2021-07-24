import moeda

m = 'R$'
p = float(input(f'Digite o preço: {m}'))
print(f'A metade de {moeda.moeda(p, m)} é {moeda.moeda(moeda.metade(p), m)}')
print(f'O dobro de  {moeda.moeda(p, m)} é {moeda.moeda(moeda.dobro(p), m)}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10), m)}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
