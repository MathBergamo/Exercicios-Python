salario = float(input('Digite o valor do seu salário: '))

if salario <= 1250:
    aumento = salario * 15 / 100
    print(f'Seu novo salário atual é de: R${aumento+salario} com 15% de aumento.')
else:
    aumento = salario * 15 / 100
    print(f'Seu novo salário atual é de: R${aumento+salario} com 10% de aumento.')

#calculando aumento salarial de 15%.
# outra forma de fazer o aumento:
# aumento = salario * 1.15