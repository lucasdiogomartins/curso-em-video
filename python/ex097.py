def escreva(msg):
    tam = len(msg) + 4
    print('~'*tam)
    # print(f'{msg:^{tam}}')  #
    print(f'  {msg}')  #
    print('~'*tam)


# Principal
escreva('Curso em Vídeo')
escreva('Oi')
escreva('Mensagem muito longa para mostrar que o tamanho é adaptável')