num = int(input('Digite um número inteiro: '))
cont = 0
for c in range(1, num+1):
    if num % c == 0:
        print('\33[33m', end = '')
        cont += 1
    else:
        print('\33[m', end='')
    print('{} \33[m'.format(c), end='')
print('\nO número \33[32m{}\33[m é divisível por \33[32m{} números'.format(num, cont))
if cont == 2:
    print('Número Primo')
else:
    print('Número Não Primo')
print('\33[m')
