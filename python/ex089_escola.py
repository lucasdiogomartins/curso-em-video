alunos = list()
while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append([nome, [nota1, nota2], media])
    resp = input('Quer continuar? [S/N]')
    if resp in 'Nn':
        break
print('-'*30)
print(f'{"N°":<4}{"NOME":<10}{"MÉDIA":>10}')
print('-'*30)
for n, a in enumerate(alunos):
    print(f'{n:<4}{a[0]:<10}{a[2]:>8.1f}')
print('-'*30)
while True:
    print('\n', '='*50)
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opc == 999:
        break
    print(f'Notas de {alunos[opc][0]}: {alunos[opc][1]}')
print(f'{"<<< FIM DO PROGRAMA >>>":^30}')
