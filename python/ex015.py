dias = int(input('Quantidade de dias alugados: '))
km = float(input('Quatidade de quilômetros rodados: '))
aluguel = dias * 60 + km * 0.15
print('O total a pagar é de R${:.2f}'.format(aluguel))
