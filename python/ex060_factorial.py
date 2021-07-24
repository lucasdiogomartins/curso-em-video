# from math import factorial  # 2

print('Digite um número positivo para ver seu fatorial')
num = int(input(' >> '))
print('='*48)
print(' {}! = '.format(num), end='')

# fact = factorial(num)  # 2

c = num  # 1
fact = 1  # 1
while c > 1:  # 1
    print('{} x '.format(c), end='')  # 1
    fact *= c  # 1
    c -= 1  # 1
print('1 = {}'.format(fact))  # 1
# print('{} '.format(fact))  # 2
print('='*48)
