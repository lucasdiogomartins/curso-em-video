pessoas = list()
pessoa = list()
maipeso = menpeso = 0

while True:
    pessoa.append(input('Nome: '))
    pessoa.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maipeso = menpeso = pessoa[1]
    else:
        if pessoa[1] >= maipeso:
            maipeso = pessoa[1]
        if pessoa[1] <= menpeso:
            menpeso = pessoa[1]
    pessoas.append(pessoa[:])
    pessoa.clear()
    resp = input('Quer continuar? [S/N] ').strip()[0]
    if resp in 'Nn':
        break
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas')
print(f'O maior peso foi {maipeso:.1f}Kg, Peso de: ', end='')
for p in pessoas:
    if p[1] == maipeso:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi {menpeso:.1f}Kg, Peso de: ', end='')
for p in pessoas:
    if p[1] == menpeso:
        print(f'[{p[0]}] ', end='')
