sair = False
cadastro = {}
pessoas = []
soma_idade = 0
mulheres = []

while sair == False:
    nome = str(input('Nome:'))
    cadastro["nome"] = nome
    sexo = str(input('Sexo [M/F]:')).lower().strip()[0]
    while sexo not in 'FfMm':
        sexo = str(input('ERRO! Digite apenas [M] ou [F]:')).lower().strip()[0]
    cadastro["sexo"] = sexo
    if sexo in 'Ff':
        mulheres.append(cadastro["nome"])
    idade = int(input('Idade:'))
    cadastro["idade"] = idade
    soma_idade += cadastro["idade"]
    usuario = str(input('Deseja continuar? [S/N]:').strip().lower()[0])
    if usuario in 'Nn':
        sair = True
    while usuario not in 'SsNn':
        usuario = str(input('ERRO! Digite apenas [S] ou [N]:').strip().lower()[0])
        if usuario in 'Nn':
            sair = True
    pessoas.append(cadastro.copy())
media = soma_idade / len(pessoas)

print(f'A) Ao todo, temos cadastrados {len(pessoas)} pessoas!')
print(f'B) A média de idade é de {media:5.2f} ')
print(f'C) As mulheres cadastradas foram:',end=' ')
for m in mulheres:
    print(f'{m}',end=', ')
print()
print(f'D) Lista das pessoas que estão acima da média:')
print(10*'-')
for p in pessoas:
    if p['idade'] >= media:

        for k,v in p.items():
            print(f'{k} = {v}',end='; ')
        print()
print(10*'-')
print(f'>>>ENCERRADO<<<')
