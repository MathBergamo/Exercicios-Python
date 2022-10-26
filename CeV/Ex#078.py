#PRIMEIRA TENTATIVA

n = []
maior = menor = 0
for c in range(0,5):
    n.append(int(input(f'digite um número para a posição {c}: ')))
    if c == 0:
        maior = menor = n[c]
    else:
        if n[c] > maior:
            maior = n[c]
        if n[c] < menor:
            menor = n[c]
print(30*'=-')
print(f'Você digitou os valores {n}')
print(f'O maior valor digitado foi: {maior}\nE o menor valor digitado foi {menor}')

#SOLUÇÃO

n = [int(input('Digite o numero 0:')),
     int(input('digite o numero 1:')),
     int(input('digite o numero 2:')),
     int(input('digite o numero 3:')),
     int(input('digite o numero 4:'))]

print('Os valores digitados foram:',end=' ')

for numero in n:
    print(numero,end=' ')

print(f"\n{25*'=-'}")

print(f'Os maiores valores digitados foram {max(n)} nas posições:',end=' ')
for posicao, numero in enumerate(n):
    if numero == max(n):
        print(posicao,end=' / ')

print(f'\nO menor valor da sequência foi: {min(n)} nas posições:',end='  ')
for posicao, numero in enumerate(n):
    if numero == min(n):
        print(posicao,end=' / ')
