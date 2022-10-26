cont = 0
s = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        cont += 1
        s += c
print(f'Houve a soma de {cont} números, resultando no valor de {s}')

