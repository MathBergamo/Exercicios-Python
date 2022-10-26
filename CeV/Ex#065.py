menor = maior = n = contador = acumulador = 0
usuario = 'sS'

while usuario not in "Nn":
    n = int(input('Digite um número:'))
    contador += 1
    if contador == 1:
        maior = n
        menor = n
    elif n > maior:
        maior = n
    elif n < menor:
        menor = n
    acumulador += n
    usuario = str(input('Quer continuar? [S/N]:')).upper().strip()[0]
print(f'Você digitou {contador} números, e a média deles é {acumulador/contador:.2f}')
print(f'O maior número digitado foi {maior} e o menor número digitado foi {menor}')

#Analisador de números que apresenta a quantidade de números digitados, o menor, o maior e a média dos valores.