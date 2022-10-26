from random import randint

def maior(*num):
    print('Analisando os valores passados:')
    bigger = 0
    for n in num:
        print(f'{n}',end=' ')
        if n == max(num):
            bigger = n
    print(f'\nForam informados {len(num)} numeros')
    print(f'O maior número encontrado foi {bigger}')
    print(20*'-=')


maior(randint(1,9),randint(1,9),randint(1,9))
maior(randint(1,9),randint(1,9),randint(1,9),randint(1,9))
maior(randint(1,9),randint(1,9),randint(1,9),randint(1,9),randint(1,9))
maior(randint(1,9))
maior(randint(1,9),randint(1,9))
maior()
