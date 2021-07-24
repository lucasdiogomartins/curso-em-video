valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = input('Quer continuar? [S/N]').strip().upper()[0]
    if resp in 'N':
        break
valores.sort(reverse=True)
print('-='*30)
print(f'Você digitou {len(valores)} elementos')
print(f'Os valores em ordem decrescente são {valores}')
print('O valor 5 ', end='')
print('não ' if 5 not in valores else '', end='')
print('foi encontrado na lista.')
