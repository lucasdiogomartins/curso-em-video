casa = float(input('Valor da casa: '))
sal = float(input('Salário do comprador: R$'))
anos = int(input('prazo em anos de financiamento: '))
prest = casa / (anos * 12)
smin = sal * 0.3
print('para pagar uma casa de R${:.2f} em {} anos '.format(casa, anos), end='')
print('a prestação será de R${:.2f}'.format(prest))

if prest <= smin:
    print('Empréstimo \33[32mCONCEDIDO!\33[m')
else:
    print('Empréstimo \33[31mNEGADO!\33[m')
