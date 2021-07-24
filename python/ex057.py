sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MF':
    print('Dados invalidos, informe novamente')
    sexo = str(input('Informe seu Sexo[M/F]: ')).strip().upper()[0]
print(sexo)