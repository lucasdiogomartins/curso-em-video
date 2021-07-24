lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')  # possivel declarar sem ()
print('-'*40)
# básica
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('-'*40)
# range
for cont in range(0, len(lanche)):
    print(f'Eu vou comer {lanche[cont]} na Posição {cont}')
print('-'*40)
# enumerate
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na Posição {pos}')

# =========

print('='*50)

# sorted
print(sorted(lanche))
print(lanche)

# unir tuplas
print('-'*30)
a = (1, 3, 5, 3)
b = (2, 4, 6, 8)
c = a + b
d = b + a
print(c, d)

# métodos
print(sorted(c))
print(len(c))
print('Contar: ', c.count(3))
print('Posição: ', c.index(8), c.index(3), c.index(3, 2))
print('='*50)

# deletar variável
pessoa = ('Lucas', 15, 'M', 56.7)
print(pessoa)
del pessoa
# 'print(pessoa)' resultaria em erro
