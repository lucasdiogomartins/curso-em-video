nome = input('Digite seu nome: ').strip()
print('\n Nome em maiúsculas:', nome.upper())
print(' Nome em minúsculas:', nome.lower())
print(' Quantidade de letras:', len(nome.replace(' ', '')))
print(' Quantidade de letras:', len(nome)-nome.count(' '))  # 2° opção
print(' Q. de letras primeiro nome:', len(nome.split()[0]))
print(' Q. de letras primeiro nome:', nome.find(' '))  # 2° opção
