def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31m * ERRO: Digite um número válido.\33[m')
            continue
        else:
            return n


def leia_float(msg):
    while True:
        try:
            n = float(input(msg).replace(',', '.'))
        except (ValueError, TypeError):
            print('\33[31m * ERRO: Digite um número válido.\33[m')
            continue
        else:
            return n


i = leia_int('Digite um número inteiro: ')
r = leia_float('Digite um número real: ')
print(f'O valor inteiro digitado foi {i} e o real foi {r}')
