from random import randint
from time import sleep


def sortear(lista):
    print('Sorteando 5 valores para a lista: ', end='')
    for c in range(0, 5):
        lista.append(randint(0, 9))
        print(lista[c], end=' ')
        sleep(0.3)
    print('- PRONTO!')


def somarpares(lista):
    s = 0
    for e in lista:
        if e % 2 == 0:
            s += e
    print(f'Somando os valores pares de {lista} temos {s}')


# Main
valores = list()
sortear(valores)
somarpares(valores)
