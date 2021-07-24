print('Gerador de PA')
print('-=-'*10)
a = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
soma = a
c = 0
while c <= 10:
    print('{}, '.format(a), end='')
    a += r
    c += 1
print('Fim')
soma = (soma + a-r) * 5
print('\nA soma dos termos vale: {}'.format(soma))
