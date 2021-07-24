lista = list()
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista')
    else:
        for p in range(0, len(lista)):
            if n <= lista[p]:
                lista.insert(p, n)
                print(f'Adicionado na posição {p} da lista')
                break
print('=-'*30)
print(f'Os valores digitados em ordem são: {lista}')
