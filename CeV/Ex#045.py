from time import sleep
from random import choice
print(f'''\n{" GAME ":=^15}\n
[1] - PEDRA
[2] - PAPEL
[3] - TESOURA''')

jogada = int(input('Digite sua jogada:'))
print('JO')
sleep(0.5)
print('QUEM?')
sleep(0.5)
print('PO')
jogadapc = choice(['Pedra', 'Papel', 'Tesoura'])

if jogadapc == 'Pedra' and jogada == 1:
    print(f'Nós empatamos! eu escolhi {jogadapc}!')
elif jogadapc == 'Pedra' and jogada == 2:
    print(f'Você ganhou! eu escollhi {jogadapc}')
elif jogadapc == 'Pedra' and jogada == 3:
    print(f'Você perdeu! eu escolhi {jogadapc}')
elif jogadapc == 'Papel' and jogada == 1:
    print(f'Você perdeu! eu escolhi {jogadapc}')
elif jogadapc == 'Papel' and jogada == 2:
    print(f'Nós empatamos! eu escolhi {jogadapc}')
elif jogadapc == 'Papel' and jogada == 3:
    print(f'Você ganhou! eu escolhi {jogadapc}')
elif jogadapc == 'Tesoura' and jogada == 1:
    print(f'Você ganhou! eu escolhi {jogadapc}')
elif jogadapc == 'Tesoura' and jogada == 2:
    print(f'Você perdeu! eu escollhi {jogadapc}')
elif jogadapc == 'Tesoura' and jogada == 3:
    print(f'Nós empatamos! eu escolhi {jogadapc}')
else:
    print('ERRO! Número escolha não válida, tente novamente!')
print('Obrigado! :)')

#Jogo de pedra, papel e tesoura.