def leia_int(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[31m * ERRO: Digite um número válido.\33[m')
            continue
        else:
            return n


def linha(tam=40, car='-'):
    print(car * tam)


def cabecalho(txt):
    linha()
    print(txt.center(40))
    linha()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    for i, e in enumerate(lista):
        print(f'\33[33m{i+1} - \33[34m{e}\33[m')
    linha()
    opc = leia_int('\33[32mSua Opção: \33[m')
    return opc
