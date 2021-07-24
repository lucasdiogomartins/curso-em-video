print('10 termos de uma PA')
first = int(input('Primeiro termo: '))
ratio = int(input('Razão: '))
terms = int(input('Quantos termos: '))
tenth = first + terms * ratio
for c in range(first, tenth, ratio):
    print(c, end=' → ')
print('Acabou')
