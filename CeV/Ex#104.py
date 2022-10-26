def leiaint(msg):
    while True:
        valor = input(msg)
        if valor.isnumeric():
            print(f'Você digitou o valor {valor}')
            return valor
        else:
            print(f'Digitou errado corno.')


#Programa principal:
n = leiaint('Digite um número inteiro:')
print(n)

