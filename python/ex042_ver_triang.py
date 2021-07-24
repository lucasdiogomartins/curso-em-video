l1 = float(input('Medida do primeiro segmento: '))
l2 = float(input('Medida do segundo segmento: '))
l3 = float(input('Medida do terceiro segmento: '))
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('Os segmentos indicados PODEM formar um triângulo ', end='')
    if l1 == l2 == l3:
        print('EQUILÁTERO.')
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print('ISÓSCELES.')
    elif l1 != l2 != l3 != l1: # elif desnecessário (else)
        print('ESCALENO.')
else:
    print('Os segmentos indicados NÃO PODEM formar um triângulo')
