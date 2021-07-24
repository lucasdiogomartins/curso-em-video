def notas(*n, sit=False):
    """
    -> calcula o total, a maior, a menor, e a média de notas da turma
    :param n: notas a serem avaliadas
    :param sit: (opcional) adiciona a situação da turma
    :return: dict com as informações da turma
    """
    dados = {
        'total': len(n),
        'maior': max(n),
        'menor': min(n),
        'média': round(sum(n) / len(n), 1)
    }
    if sit:
        if dados['média'] < 5:
            dados['situação'] = 'Ruim'
        elif dados['média'] < 6:
            dados['situação'] = 'Média'
        elif dados['média'] < 9:
            dados['situação'] = 'Boa'
        else:
            dados['situação'] = 'Ótima'
    return dados


# Main
resp = notas(5.5, 2.5, 10, 8.5, sit=True)
print(resp)
