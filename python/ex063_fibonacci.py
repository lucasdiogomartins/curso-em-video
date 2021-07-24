print('-'*30)
print('Sequência Fibonacci \n')
n = int(input('Quantidade de Termos: '))
print('-'*30)

t0 = 0
t1 = 1
print('{} -> {}'.format(t0, t1), end='')
c = 2
while c < n:
    t2 = t0 + t1
    print(' -> {}'.format(t2), end='')
    t0 = t1
    t1 = t2
    c += 1
print(' -> fim')
