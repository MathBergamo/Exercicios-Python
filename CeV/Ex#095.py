jogador = {}
jogadores = []
gols = []
sair = False

while sair == False:
    jogador["nome"] = str(input('Nome do jogador:').strip())
    partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for c in range(0,partidas):
        gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {c}?')))
    jogador['gols'] = gols.copy()
    gols.clear()
    jogador['total_gols'] = sum(jogador['gols'])
    jogadores.append(jogador.copy())
    usuario = '.'
    while usuario not in 'SsNn':
        usuario = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
        if usuario in 'Ss':
            print('continuando...')
        elif usuario in 'Nn':
            sair = True
print(30*'-=')

print(f'{"cod":<5}{"nome":<16}{"gols":<3}{"total":>16}')
print(50*'-')
for p,c in enumerate(jogadores):
    print(f'{p:<4}',end=' ')
    for v in c.values():
        print(f'{str(v):<15}',end=' ')
    print()
print(50*'-')

while True:
    dados = int(input('Mostrar dados de qual jogador? [999 Interrompe]'))
    if dados <= len(jogadores) -1:
        print(f'-- DADOS DO JOGADOR {jogadores[dados]["nome"]}')
        for p,v in enumerate(jogadores[dados]["gols"]):
            print(f'No jogo {p} fez {v} gols!')
    elif dados != 999:
        print('JOGADOR INVÁLIDO... Tente novamente!')
    else:
        print('FINALIZANDO.. VOLTE SEMPRE!!')
        break
