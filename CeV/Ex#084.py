# SOLUÇÃO 1

dados = []
pessoas = []
querSair = False

while querSair == False:
    dados.append(str(input('Nome:')).strip().capitalize())
    dados.append(int(input('Peso:')))
    pessoas.append(dados[:])
    dados.clear()
    usuario = '.'
    while usuario not in 'nNsS':
        usuario = str(input('Deseja continuar? [S/N]:')).strip().lower()[0]
        if usuario in 'Nn':
            querSair = True

gordoes = [pessoas[0]]
palitoes = [pessoas[0]]

for pessoa in pessoas[1:]:

    if pessoa[1] >= gordoes[0][1]:
        if pessoa[1] > gordoes[0][1]:
            gordoes.clear()
        gordoes.append(pessoa)
    elif pessoa[1] <= palitoes[0][1]:
        if pessoa[1] < palitoes[0][1]:
            palitoes.clear()
        palitoes.append(pessoa)

print(f'Ao todo, foram cadastrados {len(pessoas)} pessoas')
print(f'O maior peso foi de {gordoes[0][1]}')
print(f'As pessoas de maior peso foram:\n{[pessoa[0] for pessoa in gordoes]}')
print(f'O menor peso foi de {palitoes[0][1]}')
print(f'As pessoas de menor peso foram:\n{[pessoa[0] for pessoa in palitoes]}')

# SOLUÇÃO 2

pesados = leves = 0
pessoas = []
dados = []
sair = False

while sair == False:
    dados.append(str(input('Nome:')).capitalize().strip())
    dados.append(int(input('Peso:')))
    pessoas.append(dados[:])
    if len(pessoas) == 1:
        pesados = dados[1]
        leves = dados[1]
    elif dados[1] > pesados:
        pesados = dados[1]
    elif dados[1] < leves:
        leves = dados[1]
    dados.clear()
    usuario = '.'
    while usuario not in 'SsNn':
        usuario = str(input('Deseja continuar? [S/N]')).strip().lower()[0]
        if usuario in 'nN':
            sair = True

print(f'Foram cadastradas o total de {len(pessoas)} pessoas!')
print(f'O maior peso registrado foi de: {pesados}Kgs\nO nome das pessoas mais pesadas são:',end='')
for p in pessoas:
    if p[1] == pesados:
        print(p[0],end=', ')
print(f'\nO menor peso registrado foi de: {leves}Kgs\nO nome das pessoas mais leves são:',end='')
for p in pessoas:
    if p[1] == leves:
        print(p[0],end=', ')

