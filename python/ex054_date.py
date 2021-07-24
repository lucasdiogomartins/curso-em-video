from datetime import date
hoje = date.today().year
tmai = 0
tmen = 0
for p in range(1, 8):
    nasc = int(input('Em que ano a {}° pessoa nasceu? '.format(p)))
    if hoje - nasc < 18:
        tmen += 1
    else:
        tmai += 1
print('Maior idade: {} \nMenor idade: {}'.format(tmai, tmen))
