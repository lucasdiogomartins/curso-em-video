from time import sleep

ativo = True
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
mesmos = True
while ativo:
    print("="*40, '''
    [ 1 ] Somar
    [ 2 ] Multiplicar
    [ 3 ] Maior
    [ 4 ] Novos números
    [ 5 ] sair do programa
    ''')
    opç = int(input('Qual é sua opção? '))
    print('='*40)
    if opç == 1:
        print('{} + {} = {}'.format(n1, n2, n1+n2))
    elif opç == 2:
        print('{} x {} = {}'.format(n1, n2, n1*n2))
    elif opç == 3:
        maior = n1
        if n2 > n1:
            maior = n2
        print('Entre {} e {}, o MAIOR é {}'.format(n1, n2, maior))
    elif opç == 4:
        print(' - informe os novos valores - ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opç == 5:
        ativo = False
    else:
        print('* Opção inválida, tente novamente *')
    sleep(1)
