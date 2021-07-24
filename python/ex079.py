valores = list()

while True:
    val = int(input('Digite um valor: '))
    if val not in valores:
        valores.append(val)
        print('Valor adicionado com sucesso...')
    else:
        print('* Valores duplicados não são adicionados à lista...')

    resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp == 'N':
        break
print('-=-'*15)

valores.sort()
print(f'\nVocê digitou os valores: {valores}')
