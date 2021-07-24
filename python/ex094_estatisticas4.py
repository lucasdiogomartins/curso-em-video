dados = dict()
pessoas = list()
soma = media = 0
while True:
    dados['nome'] = input('Nome: ').strip().title()
    while True:  # idade
        dados['sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
        if dados['sexo'] in 'MF':
            break
        print(' * ERRO: Digite apenas M ou F!')
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    pessoas.append(dados.copy())
    dados.clear()
    while True:  # continuar ou parar
        resp = input('Quer continuar? [S/N] ').strip().upper()[0]
        if resp in 'SN':
            break
        print(' * ERRO: Digite apenas S ou N!')
    if resp == 'N':
        break
media = soma / len(pessoas)
acima = []
print('=-' * 30)
print(f' Ao todo temos {len(pessoas)} pessoas cadastradas')
print(f' A média de idade é de {media:.0f} anos')
print(' As mulheres cadastradas foram: ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(p['nome'], end=' | ')
print()
print(f' As pessoas acima da média de idade são: ')
for p in pessoas:
    if p['idade'] >= media:
        for k, v in p.items():
            print(f'    {k} = {v};  ', end='')
        print()
print('<< ENCERRADO >>')
