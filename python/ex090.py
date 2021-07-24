aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

# situação:
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
elif aluno['média'] < 5:
    aluno['situação'] = 'Reprovado'
else:
    print(' * Algo deu errado...')
print('-='*30)

# mostrar dados:
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
