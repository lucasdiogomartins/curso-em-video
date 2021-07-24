print('{:=^40}'.format(' Loja do Lusca '))
preco = float(input('Preço total das compras: R$'))
print(''' -- Formas de Pagamento -- 
[ 1 ] à vista em dinheiro/cheque
[ 2 ] à vista no cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão
''')
op = int(input(' >> '))
if 1 <= op <= 4:
    if op == 4:
        total = preco * 1.20
        vezes = int(input('em quantas parcelas? '))
        parcela = total / vezes
        print('Sua compra de {} será parcelada em {}x de '
              '{:.2f} com juros de 20 por cento, custando '
              'R${:.2f} no total'
              .format(preco, vezes, parcela, total))
    else:
        print('Sua compra de R${:.2f} '.format(preco), end='')
        if op == 1:
            total = preco * 0.9
            print('custará R${:.2f} com 10 por cento de desconto'.format(total))
        elif op == 2:
            total = preco * 0.95
            print('custará R${:.2f} com 5 por cento de desconto'.format(total))
        elif op == 3:
            total = preco
            parcela = total / 2
            print('será parcelada em 2x de {:.2f} sem juros'.format(parcela))
else:
    total = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente')
