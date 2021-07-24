from time import sleep


def analisar(* val):
    mai = 'nenhum'
    print('~'*40)
    print('Analisando os valores passados...')
    for i, v in enumerate(val):
        print(v, end=' ')
        if i == 0 or v > mai:
            mai = v
        sleep(0.3)
    print(f'- Foram informados {len(val)} valores ao todo')
    print(f'O maior valor informado foi {mai}')
    input('Aperte enter para continuar')


# Main
analisar(2, 9, 4, 5, 7, 1)
analisar(4, 7, 0)
analisar(1, 2)
analisar(6)
analisar()
