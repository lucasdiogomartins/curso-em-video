lar = float(input('Largura da Parede em metros: '))
alt = float(input('Altura da Parede em metros: '))
area = lar * alt
print('sua parede possui a dimensão de {} x {} m, e sua área é de {}m²'.format(lar, alt, area))
tinta = area/2
print('para pintá-la, precisará de {}L de tinta'.format(tinta))
