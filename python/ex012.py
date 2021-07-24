preco = float(input('Valor do Produto: R$'))
desc = int(input('Desconto (em %): '))
precod = preco - preco * desc/100
print('o valor do produto com {}% de desconto é R${:.2f}'.format(desc, precod))
