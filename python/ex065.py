resp = 's'
cont = soma = media = maior = menor = 0
while resp in 'Ss':
    num = int(input('Digite um número: '))
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = input('Quer continuar? [S/N]').upper().strip()[0]
media = soma/cont
print('Você digitou {} números \nA média entre eles é '
      '{:.2f} \no maior número é {}, e o menor foi '
      '{}'.format(cont, media, maior, menor))
