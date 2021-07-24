print('Gerador de PA \n', '-='*10)
t = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
for c in range(1, 11):
    print(t, end=' → ')
    t += r
print('PAUSA')
cont = 10
tmais = 1
while tmais != 0:
    tmais = int(input('Quantos termos você quer mostrar a mais? '))
    for c in range(0, tmais):
        print(t, end=' → ')
        t += r
        c += 1
    cont += tmais
    print('PAUSA')
print(cont, 'termos mostrados')
