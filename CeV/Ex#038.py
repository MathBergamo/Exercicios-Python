n1 = int(input('Digite um número: '))
n2 = int(input('Digite um número: '))

if n1 > n2:
    print(f'O primeiro valor {n1} é o maior que {n2}')
elif n1 < n2:
    print(f'O segundo valor {n2} é maior que {n1}')
else:
    print(f'Não existe valor maior, {n1} e {n2} são iguais')

#diferença de valores