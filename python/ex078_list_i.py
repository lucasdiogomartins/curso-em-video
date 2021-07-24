numeros = []
mai = men = 0
for p in range(0, 5):
    numeros.append(int(input(f'Digite um valor para a Posição {p}: ')))
    # estrutura substituída por max() e min()
    # if p == 0:
    #     mai = men = numeros[p]
    # else:
    #     if numeros[p] > mai:
    #         mai = numeros[p]
    #     if numeros[p] < men:
    #         men = numeros[p]
print('=-'*30)
mai = max(numeros)  #
men = min(numeros)  #
print(f'Você digitou os valores {numeros}')
print(f'\nO maior valor digitado foi {mai} nas posições ', end='')
for p, v in enumerate(numeros):
    if v == mai:
        print(f'{p}... ', end='')
print(f'\nO menor valor digitado foi {men} nas posições ', end='')
for p, v in enumerate(numeros):
    if v == men:
        print(f'{p}... ', end='')
