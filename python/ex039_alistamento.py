from datetime import date
genero = input('''-Gênero Biológico-
Digite
[M] para Masculino
[F] para Feminino
 >> ''').lower()
if genero == 'f':
    print('Sendo mulher, seu alistamento militar não é obrigatório')
elif genero == 'm':
    atual = date.today().year
    nasc = int(input('Ano de nascimento: '))
    idade = 2021 - nasc
    print('Você tem {} anos de idade em {}.'.format(idade, atual))
    if idade < 18:
        saldo = 18 - idade
        print('Ainda faltam {} anos para seu alistamento'.format(saldo))
        anoa = nasc + 18 # anoa = atual + saldo
        print('Seu alistamento será em {}'.format(anoa))
    elif idade > 18:
        saldo = idade - 18
        print('Você deveria ter se alistado há {} anos'.format(saldo))
        anoa = nasc + 18 # anoa = atual - saldo
        print('Seu alistamento foi em {}'.format(anoa))
    elif idade == 18:
        print('Você deve se alistar IMEDIATAMENTE')
    else:
        print('algo deu errado')
    
else:
    print(' *GÊNERO INVÁLIDO* ')
input()
