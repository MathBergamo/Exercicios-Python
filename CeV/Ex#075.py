num = (int(input('Digite um número:')),
    int(input('Digite um número:')),
    int(input('Digite um número:')),
    int(input('Digite um número:')))
print(f'Os valores digitados foram: {num}')
print(f'O valor 9 aparece: {num.count(9)} vez(es)')
if 3 in num:
    print(f'O valor 3 aparece na {num.index(3)+1}ª posição pela primeira vez!')
else:
    print(f'O valor 3 aparece não aparece')
print(f'Os números pares digitados foram:', end=' ')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')


