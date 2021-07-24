def fatorial(num, show=False):
    """
    -> Calcula o fatorial de um número
    :param num: Número a ser calculado
    :param show: Mostrar a conta (opcional)
    :return: fatorial do número
    """
    f = 1
    conta = ''
    for c in range(num, 0, -1):
        f *= c
        if show:
            conta += str(c)
            if c > 1:
                conta += ' x '
            else:
                conta += ' = '
    return conta + str(f) if show else f


print('-' * 30)
print(fatorial(5, show=True))
help(fatorial)
