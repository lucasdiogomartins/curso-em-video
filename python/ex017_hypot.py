from math import hypot

co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = (co**2 + ca**2)**(1/2)
print('a hipotenusa vale {:.2f}'.format(h))

hip = hypot(co, ca)
print('hipotenusa calculada por .math: {:.2f}'.format(hip))
