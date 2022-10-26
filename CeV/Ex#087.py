matriz = [[0,0,0],[0,0,0],[0,0,0]]
pares = ter_coluna = maior_seg_linha = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite o valor de [{l+1}]/[{c+1}]:'))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]
        if c == 2:
            ter_coluna += matriz[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print(f'A soma dos valores pares é: {pares}')
print(f'A soma dos valores da 3ª coluna é: {ter_coluna}')
print(f'O maior valor da segunda linha é: {max(matriz[1])}')

#2 SOLUÇÃO

matriz = [[],[],[]]
pares = soma_coluna = maior_linha = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Número [{l}]/[{c}]:')))
        if matriz[l][c] % 2 == 0:
            pares += matriz[l][c]

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]:^5}]',end='')
    print()

print(f'A soma de todos os valores pares digitados foi: {pares}')
for l in range(0,3):
    soma_coluna += matriz[l][2]
print(f'A soma dos valores da terceira coluna é de: {soma_coluna}')
for c in range(0,3):
    if c == 0:
        maior_linha = matriz[1][c]
    elif matriz[1][c] > maior_linha:
        maior_linha = matriz[1][c]
print(f'O maior valor da segunda linha é: {maior_linha}')
