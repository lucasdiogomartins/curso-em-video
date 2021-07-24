real = float(input('Quanto dinheiro você possui? R$'))
dolar = real / 5.26
euro = real / 6.47
libra = real / 7.17
iene = real / 0.051
print('Com R${} em Jan de 2021, você pode comprar:'.format(real))
print('Dólar: US${:.2f}'.format(dolar))
print('Euro: US${:.2f}'.format(euro))
print('Libra: US${:.2f}'.format(libra))
print('Iene: US${:.2f}'.format(iene))
