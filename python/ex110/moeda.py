def aumentar(preco=0, taxa=0, form=False):
    res = preco + (preco * taxa/100)
    return res if not form else moeda(res)


def diminuir(preco=0, taxa=0, form=False):
    res = preco - (preco * taxa/100)
    return res if form is False else moeda(res)


def dobro(preco=0, form=False):
    res = preco * 2
    return res if not form else moeda(res)


def metade(preco=0, form=False):
    res = preco / 2
    return res if form is False else moeda(res)


def moeda(preco=0.0, moeda_='R$'):
    return f'{moeda_}{preco:.2f}'.replace('.', ',')


def resumo(preco=0, aum=0, dim=0):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{f"{aum}% de aumento:":19} {aumentar(preco, aum, True)}')
    print(f'{f"{dim}% de redução:":19} {diminuir(preco, dim, True)}')
    print('-' * 35)
# \t para tabulação
