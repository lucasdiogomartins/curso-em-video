from datetime import date

nasc = int(input('Ano de nascimento do atleta: '))
hoje = date.today().year
idade = hoje - nasc
print('Idade: {} anos \nEste atleta está classificado como '.format(idade), end='')
if idade <= 9:
    print('Mirim')
elif idade <= 14:
    print('Infantil')
elif idade <= 19:
    print('Junior')
elif idade <= 25:
    print('Sênior')
else:
    print('Master')