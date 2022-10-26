from time import sleep
print(10*'x:')
print(' ✖x✖ TABUADA ✖x✖ ')
print(10*'x:')
n = count = 0

while True:
    print(f'{45 * "-"}')
    n = int(input('Digite um número:'))
    print(f'{45 * "-"}')
    count = count - count
    if n < 0:
        break
    while count < 10:
        count += 1
        print(f'{n} x {count} = {n*count}')
print('Encerrando programa...')
sleep(2)
print('Programa encerrado. Volte sempre \n:)')

# 2 FORMA DE FAZER COM FOR

while True:
    n = int(input('Digite um número'))
    if n < 0:
        break
    for c in range(1, 10):
        print(f'{n} x {c} = {n*c}')

#Tabuada feita com as duas estruturas de repetição