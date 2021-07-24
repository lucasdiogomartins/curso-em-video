mai_idade = homens = fem_men_20 = 0
while True:
    print('-'*30)
    print('CADASTRE UMA PESSOA')

    # inserir dados
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()[0]
    while sexo not in 'MF':
        sexo = input('ERRO. Digite novamente o sexo: ').strip().upper()[0]

    # verificar e adicionar nas estatisticas
    if idade >= 18:
        mai_idade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        fem_men_20 += 1

    # adicionar ou encerrar cadastros
    continuar = input('Quer continuar? [S/N]: ').strip().upper()[0]
    while continuar not in 'SN':
        continuar = input('ERRO. Quer continuar? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break
# mostrar estatisticas
print(f'''Total de pessoas com mais de 18 anos: {mai_idade}
Ao toto temos {homens} homens cadastrados
E temos {fem_men_20} mulheres com menos de 20 anos''')
