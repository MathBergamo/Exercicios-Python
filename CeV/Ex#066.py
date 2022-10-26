print('SOMADOR AMBULANTE COM BREAK!')
soma = count = 0

while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    soma += n
    count += 1
print(f'Você digitou {count} números, e a soma deles foi {soma}')

#Somador do ex65 feito com break