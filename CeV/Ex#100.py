#PRIMEIRA TENTATIVA

from random import randint

def sorteia(num):
    for c in range(0,5):
        num.append(randint(1,9))
    print(f'Os números adicionados à lista foram: {numeros}')
    print(30*"=-")

def somaPar(num2):
    pares = 0
    print(f'Os números pares encontrados da lista foram:',end=' ')
    for n in num2:
        if n % 2 == 0:
            pares += n
            print(n,end=' ')
    print(f'\nA Soma de todos os números pares é: {pares}')

numeros = []
sorteia(numeros)
somaPar(numeros)
