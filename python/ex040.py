nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2) / 2
print('Média = {:.1f}'.format(media))
if media < 5.0:
    print('Aluno REPROVADO!')
elif 5 <= media < 7:
    print('Aluno está em RECUPERAÇÃO')
elif 7 <= media <= 10:
    print('Aluno APROVADO')
else:
    print(' * Há algo de errado * ')
