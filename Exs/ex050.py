def somar_pares(num):
    if num % 2 == 0:
        return num
    else:
        return 0

soma_total = 0

for c in range(1,7):
    num = somar_pares(int(input('Digite um número:')))
    soma_total += num

print(f'A soma de todos os pares foi de {soma_total}')