jogador = {'nome': str(input('Nome:').capitalize())}
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
gols_l = []
jogador['gols'] = gols_l
tot_gols = 0

for j in range(0, partidas):
    gols_l.append(int(input(f'Quantos gols {jogador["nome"]} fez na {j} partida?:')))
    tot_gols += gols_l[j]
jogador['total'] = tot_gols
print(jogador)
print(30*'-=')
for k, v in jogador.items():
    print(f'O {k} tem o valor {v}')
print(30*'-=')

print(f'O jogador {jogador["nome"]} jogou {partidas} partidas')

for i, v in enumerate(jogador['gols']):
    print(f' -> Na partida {i} {jogador["nome"]} fez {v} gols!')
print(f'Foi um total de {jogador["total"]} gols!')
