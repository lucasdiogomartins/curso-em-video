matriz = [[], [], []]
som_par = som_c2 = mai_l1 = 0

# adicionar valores
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite o valor para [{l}, {c}]: ')))
print('-=' * 30)

# mostrar tabela e calcular estatisticas
for lin in range(0, 3):
    for c, e in enumerate(matriz[lin]):
        print(f'[{e:^5}]', end='')
        if e % 2 == 0:
            som_par += e
        if c == 2:
            som_c2 += e
        if lin == 1 and e > mai_l1:
            mai_l1 = e
    print()
print('-=' * 30)

# mostrar estatisticas
print(f'A soma dos valores pares é {som_par}')
print(f'A soma dos valores da terceira coluna é {som_c2}')
print(f'O maior valor da segunda linha é {mai_l1}')
