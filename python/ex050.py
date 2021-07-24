soma = 0
cont = 0
print('Digite 6 números inteiros')
for c in range(1, 7):
    num = int(input('{}° número: '.format(c)))
    if num % 2 == 0:
        soma += num
        cont += 1
print('A soma dos {} valores pares é {}'.format(cont, soma))
