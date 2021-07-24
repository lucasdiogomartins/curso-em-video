def leia_dinheiro(msg):
    while True:
        preco = str(input(msg)).replace(',', '.').strip()
        if preco.isalpha() or preco == "":
            print(f'\33[31mERRO: "{preco}" é um preço inválido!\33[m')
        else:
            break
    return float(preco)
