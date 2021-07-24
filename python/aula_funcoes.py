def titulo(msg):
    print('-'*30)
    print(f'{msg:^30}')
    print('-'*30)


def soma(a, b):
    print(f'{a} + {b} = {a+b}')


def contador(*val):  # * desempacotamento
    tam = len(val)
    print(f'O tamanho de {val} = {tam}')


def dobrar(lst):
    for p in range(0, len(lst)):
        lst[p] *= 2
    print(f'Lista dobrada: {lst}')


def somatodos(* val):  # * desempacotamento
    s = 0
    for num in val:
        s += num
    print(f'A soma de {val} é {s}')


# Programa principal
titulo('== Funções ==')
soma(5, 7)
soma(b=6, a=11)
contador(1, 3, 5, 2, 6)
valores = [1, 5, 4, 8, 10]
dobrar(valores)
somatodos(2, 5, 4, 48, 12, 1)

print()


# == FUNÇÕES 2 ==
titulo('== Funções 2 ==')


# DOCSTRINGS em Funções e Parâmetros padrão/opcional
def somar(a=0, b=0, c=0):  # 'param' = 0 para definir como padrão/opcional
    """
    -> soma os parâmetros passados e printa na tela
        - caso não passe um parâmetro, o mesmo valerá 0
    :param a: soma com param b e c
    :param b: soma com param a e c
    :param c: soma com param a e b
    :return: sem retorno
    Função criada por Lucas Diogo Martins
    """
    s = a + b + c
    print(f'A soma vale {s}')


help(somar)
somar(1, 3, 6)
somar(5, 11)
somar(b=4, c=6)
print('\n', '~'*40)


# Retorno de valores
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f  # retorna o valor da variável f


f1 = fatorial(4)
f2 = fatorial(5)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}.')
print('\n', '~'*40)


# Retorno Booleano
def par(n):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um número: '))
if par(num):
    print('é par')
else:
    print('não é par')
