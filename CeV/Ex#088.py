#1 SOLUÇÃO
from random import sample
from time import sleep

print(25*'=-')
print(f'{"JOGOS DA SENA!":^50}')
print(25*'=-')

usuario = int(input('Quantos jogos que você quer?'))

print(f'\nSORTEANDO {usuario} JOGOS!')
print(50*'=')

for c in range(0, usuario):
    numeros = sample(range(60), 6)
    sleep(0.5)
    print(f'Jogo {c+1}: {numeros}')

print(10*'->',"BOA SORTE",10*'<-')
