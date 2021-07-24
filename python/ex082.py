lista = []
pares = []
impares = []
while True:  # adicionar valores
    lista.append(int(input('Digite um número: ')))
    resp = input('Quer continuar? [S/N] ').strip().upper()[0]
    if resp == 'N':
        break
for v in lista:  # adicionar às listas "pares" e "impares"
    if v % 2 == 0:
        pares.append(v)
    elif v % 2 == 1:
        impares.append(v)
print('-='*30)
print(f'A lista completa é {lista}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
