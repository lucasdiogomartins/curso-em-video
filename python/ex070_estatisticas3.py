print('='*40)
print(f'{"Loja Do Lusca":^40}')
print('='*40)

# variaveis iniciais
totalR = totMil = pBarato = cont = 0
nBarato = ' '

# compras
while True:
    # inserir dados
    nomeP = input('Nome do Produto: ').strip()
    preco = float(input('Preço: R$'))

    # verificar estatisticas
    totalR += preco
    if preco >= 1000:
        totMil += 1
    if cont == 0 or preco < pBarato:
        pBarato = preco
        nBarato = nomeP
    cont += 1

    # continuar ou encerrar
    continuar = ' '
    while continuar not in 'SN':
        continuar = input('Continuar compras? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break

# encerramento
print('{:-^40}'.format("FIM DO PROGRAMA"))
print(f'''O total de compra foi {totalR:.2f};
Temos {totMil} produtos custando R$1000,00 ou mais;
O produto mais barato foi "{nBarato}" que custa R${pBarato:.2f}.''')
