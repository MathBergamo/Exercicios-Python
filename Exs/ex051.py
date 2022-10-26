def pa(termo,razao):
    for c in range(0,11):
        print(termo, end=' > ') if c < 10 else print('FIM')
        termo += razao

print('PROGRESSÃO ARITMÉTICA - 10 TERMOS')
resultado = pa(int(input('Digite o termo:')),int(input('Digite a razão:')))