from cursoemvideo.ex115.lib.interface import *


def arquivo_existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        a = open(nome, 'wt+', encoding='utf-8')
        a.close()
    except:
        print('Ocorreu um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def ler_arquivo(nome):
    try:
        a = open(nome, 'rt', encoding='utf-8')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabecalho('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
    finally:
        a.close()


def cadastrar(arq, nome='desconhecido', idade=0):
    try:
        a = open(arq, 'at', encoding='utf-8')
    except:
        print('Houve um ERRO ao abrir o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um ERRO ao escrever no arquivo')
        else:
            cabecalho('pessoa cadastrada com sucesso!')
            a.close()
