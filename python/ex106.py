from time import sleep

cores = ['\033[m',         # 0 - sem cores
         '\033[1;41m',  # 1 - vermelho
         '\033[1;42m',  # 2 - verde
         '\033[1;43m',  # 3 - amarelo
         '\033[1;44m',  # 4 - azul
         '\033[7;38m',  # 5 - branco
         ]


def titulo(msg='', cor=0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(cores[0], end='')
    sleep(1)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(cores[5], end='')
    help(com)
    print(cores[0], end='')
    sleep(2)


# Main
titulo('SISTEMA DE AJUDA PyHELP', 2)
while True:
    comando = input('Função ou Biblioteca > ').strip().lower()
    if comando == 'fim':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO', 1)
