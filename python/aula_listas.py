num = [1, 3, 5, 8]
print(num)
num[2] = 4  # tira o 5 e coloca o 4
print(num)
num.append(10)  # adiciona elemento à lista
print(num)
num.insert(3, 2)  # insere, na posição x, o elemento y -- (3, 2)
#          x  y
print(num)

# ordenar
print('')
num.sort()  # ordena elementos
print(num)
num.sort(reverse=True)  # ordena elementos ao contrario
print(num)

# eliminar
print('')
num.pop()  # retira o último elemento da lista
print(num)
num.pop(2)  # remove o elemento da posição x -- (2)
print(num)
del num[0]  # funciona como .pop()
print(num)
num.remove(8)  # remove o elemento x -- (8); se não existir x, resulta erro
print(num)
# maneira de remover sem risco de erro
if 7 in num:
    num.remove(7)
else:
    print(' * elemento não encontrado\n')

print(f'Essa lista possui {len(num)} elementos\n\n')  # comprimento da lista


valores = list()  # lista vazia; pode ser usado '[]'
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}, ', end='')
print('')

# for cont in range(0, 3):
#     valores.append((int(input('Digite um valor: '))))
for c, v in enumerate(valores):
    print(f'Na posição {c}, há o valor {v}')
print('fim da lista\n\n')

a = [2, 3, 4, 7]
b = a  # criou uma ligação entre a lista a e b
b[2] = 8
print(f'Lista a = {a}')
print(f'Lista b = {b}')
b = a[:]  # b recebe todos os elementos de a (cópia)
b[2] = 6
print(f'Cópia b = {b}')
print('='*30)

# LISTAS 2
galera = [['Joao', 19], ['Maria', 23], ['Joaquim', 45]]
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
print('-'*30)

pessoas = list()
dado = list()
for c in range(0, 5):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    pessoas.append(dado[:])  # [:] para criar uma cópia da lista 'dados'
    dado.clear()
for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
    else:
        print(f'{p[0]} é menor de idade')
