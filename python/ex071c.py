print('='*30)
print('{:^30}'.format('Banco CeV'))
print('='*30)
valor = int(input('Que valor você quer sacar? R$'))
print('Total de:')

ced = 50
totced = 0
while True:
    if valor >= ced:  # contar cédulas
        totced += 1
        valor -= ced
    else:  # trocar valor da cédula
        print(f'{totced} cédulas de R${ced}\n' if totced > 0 else '', end='')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0  # resetar contagem de cédulas a cada loop
        if valor == 0:
            break
print('='*30)
print('Volte Sempre!')