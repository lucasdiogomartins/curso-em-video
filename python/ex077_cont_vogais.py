palavras = ('Sucesso', 'Demolir', 'Manicure', 'Assustar', 'Visita',
            'Magnitude', 'Ensinar', 'Colecções', 'Biblioteca', 'Curral')
for p in palavras:
    print(f'\nNa palavra  {p.upper():<10} temos: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
