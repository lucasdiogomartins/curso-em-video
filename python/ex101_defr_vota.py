def vota(nasc):
    from datetime import date  # import local de biblioteca

    idade = date.today().year - nasc

    if idade < 16:
        return f'Com {idade} anos, NÃO VOTA'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos, VOTO OPCIONAL'
    else:
        return f'Com {idade} anos, VOTO OBRIGATÓRIO'


# Main
ano = int(input('Em que ano você nasceu? '))
print(vota(ano))
