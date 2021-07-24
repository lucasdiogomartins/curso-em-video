# Dicionarios
pessoas = {'nome': 'Lucas', 'sexo': 'M', 'idade': 15}

# Metodos
print(pessoas['nome'])
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())
for k, v in pessoas.items():
    print(f'{k} = {v}')
print()

# Modificar valores
del pessoas['sexo']
pessoas['nome'] = 'Josias'
pessoas['altura'] = 1.79
print(pessoas)
print()

# Dicionarios em Listas
brasil = []
estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(f'UF RJ: {brasil[0]["uf"]} \nSigla São Paulo: {brasil[1]["sigla"]}')
print()

# Ler valores
"""estado = dict()
brasil = list()
for c in range(0, 2):
    estado['uf'] = input('Unidade Federativa: ')
    estado['sigla'] = input('Sigla do Estado: ')
    brasil.append(estado.copy())  # copiar dicionarios = .copy()
for e in brasil:
    for k, v in e.items():
        print(f'{k}: {v}', end='    ')
    print()"""  # tirar """ """

from operator import itemgetter
dicio = {'a': 2, 'b': 3, 'c': 1}
# v dicionario organizado em uma lista v
rank = sorted(dicio.items(), key=itemgetter(1))
#      sorted('''''.items(), key=itemgetter("0: key, 1: value"), reverse
print(dicio, ' --- ', rank)
