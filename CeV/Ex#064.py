print('SOMADOR AMBULANTE!')
n = int(input('Digite um número [999 irá parar]:'))

acumulador = n
contador = 0
while n != 999:
    n = int(input('Digite um número [999 irá parar]:'))
    acumulador += n if n != 999 else 0
    contador += 1
print(f'A soma foi {acumulador} de {contador} números digitados.')

#2 FORMA

cont = soma = 0
num = int(input('Digite um número [999 irá parar]:'))
while num != 999:
    soma += num
    cont += 1
    num = int(input('Digite um número [999 irá parar]:'))
print(f'Você digitou {cont} números e a soma entre eles foi {soma}')

#Somador com operadores itnerários.