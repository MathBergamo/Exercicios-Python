from random import randint
from time import sleep
from operator import itemgetter

jogadores = {
    'jogador1': randint(1, 6),
    'jogador2': randint(1, 6),
    'jogador3': randint(1, 6),
    'jogador4': randint(1, 6)
}

print('Valores sorteados:')
for k, v in jogadores.items():
    sleep(0.7)
    print(f'O {k} tirou {v} no dado!')

count = 1

for j in sorted(jogadores.items(), key=itemgetter(1), reverse=True):
    sleep(0.7)
    print(f'Em {count}º lugar: {j[0]} tirou o valor de: {j[1]}')
    count += 1

