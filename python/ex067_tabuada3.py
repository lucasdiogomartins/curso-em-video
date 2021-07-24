while True:
    num = int(input('Valor da Tabuada: '))
    print('-'*30)
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num*c}')
    print('-'*30)
print('Programa de tabuada ENCERRADO. Volte sempre!')
