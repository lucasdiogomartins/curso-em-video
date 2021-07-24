from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: ')).capitalize()
dados['idade'] = date.today().year - int(input('Ano de Nascimento: '))
dados['ctps'] = int(input('Carteira de Trabalho (0 caso não tenha): '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + (dados['contratação'] + 35) - date.today().year
print('=-' * 30)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
# krl esse foi foda man...
