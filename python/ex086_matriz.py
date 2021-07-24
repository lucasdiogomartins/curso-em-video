matriz = [[], [], []]
mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(input(f'Digite um elemento para [{l}, {c}]: '))
for l in matriz:
    for c in l:
        if len(c) > mai:
            mai = len(c)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^{mai}}]', end='')
    print()
