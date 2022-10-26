# 1 SOLUÇÃO

lista = []
usuario = 's'

while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    usuario = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if usuario in 'Nn':
        break

lista.reverse()
print(f'\nOs numeros digitados foram {lista}')
print(f'Foram digitados {len(lista)} elementos')
if 5 in lista:
    print('O valor 5 foi encontrado na lista')
else:
    print('O valor 5 não foi encontrado na lista')

# 2 SOLUÇÃO

lista = []
pos = 0
usuario = 's'

while usuario not in 'Nn':
    n = int(input('Digite um número:'))
    if pos == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado na última posição..')
    else:
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
    usuario = str(input('Quer continuar? [S/N]')).strip().lower()[0]

lista.reverse()
print(f'Foram digitados os numeros {lista}')
print(f'Temos {len(lista)} elementos')
if 5 in lista:
    print('Foi encontrado o número 5 na lista')
else:
    print('Não foi encontrado o número 5 na lista')

