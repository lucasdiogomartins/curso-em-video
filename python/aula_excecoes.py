try:
    a = float(input('Numerador: '))
    b = float(input('Denominador: '))
    r = a / b
except:
    print('Infelizmente tivemos um problema :(')
else:
    print(f'O resultado de {a} / {b} é {r:.1f}')
finally:
    print('Volte sempre!')

print()  # ============================================
try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('Tivemos um problema de tipos de dados que você digitou')
except ZeroDivisionError:
    print('Impossível dividir um número por zero')
except KeyboardInterrupt:
    print('O usuário não informou os dados')
except Exception as erro:
    print(f'Ocorreu um erro: {erro.__cause__}')
else:
    print(r)
