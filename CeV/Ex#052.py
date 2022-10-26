print('\033[34mNÚMERO PRIMO')
contador = 0
n = int(input('\033[mDigite um número: '))
for c in range(1, n+1):
    if n % c == 0:
        print(f'\033[34m{c}', end=' ')
        contador += 1
    else:
        print(f'\033[31m{c}', end=' ')
print(f'\033[m\nO número {n} é divisível {contador} vezes.')
if contador == 2:
    print(f'\033[34mO número {n} É PRIMO!')
else:
    print(f'\033[34mO número {n} NÃO É PRIMO!')

#Verifica se o número é ou não primo.