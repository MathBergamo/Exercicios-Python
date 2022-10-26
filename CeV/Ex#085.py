numeros = [[],[]]

for n in range(0, 7):
    num = int(input(f'Nº{n+1}:'))
    if num % 2 == 1:
        numeros[1].append(num)
    elif num % 2 == 0:
        numeros[0].append(num)

numeros[1].sort()
numeros[0].sort()

print(f'Os valores ímpares digitados foram:{numeros[1]}')
print(f'Os valores pares digitados foram:{numeros[0]}')
