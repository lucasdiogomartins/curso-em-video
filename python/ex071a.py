print('='*30)
print(f'{"Banco":^30}')
print('='*30)
valor = int(input('Qual valor você quer sacar? R$'))
c50 = c20 = c10 = c1 = 0
while True:
    if valor >= 50:
        c50 += 1
        valor -= 50
    else:
        break
while True:
    if valor >= 20:
        c20 += 1
        valor -= 20
    else:
        break
while True:
    if valor >= 10:
        c10 += 1
        valor -= 10
    else:
        break
while True:
    if valor >= 1:
        c1 += 1
        valor -= 1
    else:
        break
print('-'*30)
print(f'''Total de:
{c50} cédulas de 50,00
{c20} cédulas de 20,00
{c10} cédulas de 10,00
{c1} cédulas de 1,00''')
print('-'*30)
print('Volte sempre!')