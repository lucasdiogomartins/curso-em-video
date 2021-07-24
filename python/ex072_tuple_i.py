while True:
    numeros = ('zero', 'um', 'dois', 'três', 'quatro',
               'cinco', 'seis', 'sete', 'oito', 'nove',
               'dez', 'onze', 'doze', 'treze', 'quatorze',
               'quinze', 'dezesseis', 'dezessete', 'dezoito',
               'dezenove', 'vinte')
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if not 0 <= num <= 20:
            print('Tente novamente. ', end='')
        else:
            break
    print(f'Você digitou o número {numeros[num]}')
    print('='*30)
    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
