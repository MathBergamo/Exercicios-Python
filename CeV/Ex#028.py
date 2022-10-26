from random import randint
from time import sleep
usuario = int(input('Digite um número de 1 a 5:'))
numero = randint(1, 5)

print('Processando...')
sleep(2)
if usuario == numero:
    print(f'Parabéns, você acertou! o número sorteado foi {numero}')
else:
    print(f'Que pena, o número sorteado foi {numero} tente novamente!')

#Biblioteca time com a função sleep, que causa um delay de acordo com o valor númerico colocado nela.
