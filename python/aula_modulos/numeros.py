import uteis  # Mais recomendado
# from uteis import fatorial, dobro  # Não utilizar

num = int(input('Digite um número: '))
fat = uteis.fatorial(num)  # import
# fat = fatorial(num)  # from import
print(f'O fatorial de {num} é {fat}')
print(f'O dobro de {num} é {uteis.dobro(num)}')
