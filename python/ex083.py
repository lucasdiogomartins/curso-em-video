expressao = input('Digite a expressão numérica: ').strip()
pilha = []
for elem in expressao:
    if elem == '(':
        pilha.append('(')
    elif elem == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
print('Sua expressão está ', end='')
print('correta!' if len(pilha) == 0 else 'incorreta')
