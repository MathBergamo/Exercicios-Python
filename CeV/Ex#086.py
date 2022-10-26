#1 Solução

matriz = [[],[],[]]

for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite o número [{l}]/[{c}]:')))

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]}]',end='')
    print()

#2 SOLUÇÃO

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'VALOR PARA [{i}, {j}]: '))

for l in matriz:
    print(f'{l}')
