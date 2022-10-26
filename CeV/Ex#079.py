numeros = []
while True:
    n = int(input('Digite um valor:'))
    if n not in numeros:
        numeros.append(n)
    else:
        print('Valor duplicado! Não será adicionado..')
    usuario = str(input('Quer continuar? [S/N] ')).strip().lower()[0]
    if usuario in 'Nn':
        break
print(30*'=-')
numeros.sort()
print(f'Os valores digitados foram: {sorted(numeros)}')
