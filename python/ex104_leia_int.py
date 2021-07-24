def leia_int(msg=''):
    while True:
        n = input(f'{msg}').strip()
        if n.isnumeric():
            return int(n)
        else:
            print('\33[1;31mERRO: Digite um número inteiro válido\33[m')


# Main
num = leia_int('Digite um número: ')
print(f'Você digitou o número {num}')

# Refazer ex104 caso não funcione corretamente
