somai = 0  # soma da idade
idadehmv = 0  # idade homem mais velho
nomehmv = ''  # nome homem mais velho
totm20 = 0  # total de mulheres com menos de 20 (anos)
for p in range(1, 5):
    print('-----{}° Pessoa-----'.format(p))
    nome = input('Nome: ').strip().capitalize()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip()

    somai += idade
    if sexo in 'Mm' and idade > idadehmv:  # in == esta contido em
        idadehmv = idade
        nomehmv = nome 
    if sexo in 'Ff' and idade < 20:
        totm20 += 1

mediai = somai / 4

print('\nA média de idade do grupo é de {} anos'.format(mediai))
print('O homem mais velho tem {} anos e se chama {}'.format(idadehmv, nomehmv))
print('Ao todo são {} mulheres com menos de 20 anos'.format(totm20))
input()
