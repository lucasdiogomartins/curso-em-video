numeros = (int(input('Digite um número: ')),
           int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')),
           int(input('Digite o último número: ')))
print('='*30, f'\nOs números digitados foram: ', end='')
for n in numeros:
    print(n, end=' ')
# estatisticas
print(f'\nO valor 9 apareceu {numeros.count(9)} vezes')
print(f'O valor 3 apareceu na posição {numeros.index(3)+1}'
      if 3 in numeros
      else 'O valor 3 não apareceu em nenhuma posição')
print(f'Os números pares digitados foram: ', end='')
for n in numeros:
    if n % 2 == 0:
        print(n, end=' ')
