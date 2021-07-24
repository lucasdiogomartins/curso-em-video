from time import sleep


def contagem(i, f, p):
    print('~' * 40)
    if p == 0:  # Segunda opção para p == 0
        print('passo = 1')
        p = 1  # end
    if p < 0:
        p = -p  # p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(1)
    if i <= f:
        while i <= f:
            print(i, end=' ')
            i += p
            sleep(0.3)
    else:
        while i >= f:
            print(i, end=' ')
            i -= p
            sleep(0.3)
    print('FIM')
    print()


# Principal
contagem(1, 10, 1)
contagem(10, 0, 2)
print('='*50)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim: '))
while True:  # Opção para p == 0
    pas = int(input('Passo: '))
    if pas != 0:
        break
    print(' * ERRO: digite um valor diferente de 0!')
contagem(ini, fim, pas)
