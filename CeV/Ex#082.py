# 1 SOLUÇÃO

lista = []
lista_Impar = []
lista_Par = []

while True:
    n = int(input('Digite um número:'))
    lista.append(n)
    if n % 2 == 0:
        lista_Par.append(n)
    elif n % 2 == 1:
        lista_Impar.append(n)
    usuario = str(input('Quer continuar? [S/N]')).strip().lower()[0]
    if usuario in 'Nn':
        break

print(f'Lista completa {lista}')
print(f'Lista de ímpares {lista_Impar}')
print(f'Lista de pares {lista_Par}')

# 2 solução

lista = []
par = []
impar = []

while True:
    lista.append(int(input('Digite um número:')))
    usuario = str(input('Deseja continuar? [S/N]')).lower().strip()[0]
    if usuario in 'Nn':
        break
for n in lista:
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)

print(f'Lista completa {lista}')
print(f'Lista Ímpar {impar}')
print(f'Lista par {par}')

