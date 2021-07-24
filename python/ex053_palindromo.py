print('Digite uma frase para verificar se ela é um palíndromo (não utilize acentos)')
frase = str(input('> ')).strip().upper().replace(' ', '')
inverso = frase[::-1]
# for letra in range(len(frase)-1, -1, -1):
#    inverso += frase[letra]
print('{} de trás para frente é {}'.format(frase, inverso))
if inverso == frase:
    print('Temos um palíndromo!')
else:
    print('Esta frase não é um palíndromo')
