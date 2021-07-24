from lib.interface import *
from lib.arquivo import *
from time import sleep

arq = 'bancodedados.txt'

if not arquivo_existe(arq):
    criar_arquivo(arq)

while True:
    resp = menu(['Mostrar pessoas cadastradas',
                 'Cadastrar nova pessoa', 'Sair do Sistema'])
    if resp == 1:
        # listar conteúdo de um arquivo
        ler_arquivo(arq)
    elif resp == 2:
        cabecalho('CADASTRAR PESSOA')
        nome = str(input('NOME: '))
        idade = leia_int('IDADE: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        print('Opção 3')
        break
    else:
        print('\33[31m* ERRO: Digite uma opção válida\33[m')
    sleep(1)
