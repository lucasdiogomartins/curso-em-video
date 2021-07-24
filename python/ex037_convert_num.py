num = int(input('Número inteiro: '))
print('''Escolha uma das bases de conversão: 
[1] converter para BINÁRIO
[2] converter para OCTAL
[3] converter para HEXADECIMAL''')
op = int(input('> '))
if op == 1:
    print('{} em binário é {}'.format(num, bin(num)[2:]))
elif op == 2:
    print('{} em octal é {}'.format(num, oct(num)[2:]))
elif op == 3:
    print('{} em hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('\33[3;31m OPÇÃO INVÁLIDA \33[m')
input('Pressione [ENTER] para continuar')
