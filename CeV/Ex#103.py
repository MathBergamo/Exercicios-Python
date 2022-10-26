def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gol(s)!')


print(20*'-')
n = str(input('Nome:'))
g = str(input('Gols:'))
if g.isnumeric():
    g = int(g)
else:
    g = '<inválido>'
if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n,g)
