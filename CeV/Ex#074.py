#PRIMEIRA TENTATIVA

from random import randint

tupla = maior = menor = valores = 0

for c in range(0, 6):
    random = randint(0,10)
    print(random,end=' ')
    if c == 1:
        maior = random
        menor = random
    elif random > maior:
        maior = random
    elif random < menor:
        menor = random
print(f'\n{maior}\n{menor}')

#SOLUÇÃO FINAL

from random import randint

n = (randint(1,10)), (randint(1,10)), (randint(1,10)), (randint(1,10)), (randint(1,10))
count = maior = menor = 0

print(f'os valores sorteados foram:', end='')

for c in n:
    print(f' {c}',end='')
    count += 1
    if count == 1:
        maior = c
        menor = c
    elif c > maior:
        maior = c
    elif c < menor:
        menor = c
print(f'\nO maior número foi: {maior}\nEnquanto o menor foi: {menor}')

#SOLUÇAO COM MIN/MAX

from random import randint

n = (randint(1,10)), (randint(1,10)), (randint(1,10)), (randint(1,10)), (randint(1,10))

print(f'os valores sorteados foram:', end='')

for c in n:
    print(f' {c}',end='')
print(f'\nO maior número foi: {max(n)}\nEnquanto o menor foi: {min(n)}')
