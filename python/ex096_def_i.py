def area(x, y):
    a = x * y
    print(f'A área de um terreno {x:.1f}x{y:.1f}m é {a:.1f}m²')


# Principal
print('  Controle de Terrenos  ')
print('-'*24)
lar = float(input('Largura do terreno (m): '))
comp = float(input('Comprimento do terreno (m): '))
area(lar, comp)
