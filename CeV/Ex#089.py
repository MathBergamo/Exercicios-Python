# PRIMEIRA TENTATIVA
alunos = []
dados = []
media = []
soma = []
sair = False
sair2 = False
count = 0

while sair == False:
    dados.append(str(input('Nome:')).capitalize().strip())
    dados.append(float(input('Nota 1:')))
    dados.append(float(input('Nota 2:')))
    alunos.append(dados[:])
    media.append((dados[1] + dados[2]) / 2)
    dados.clear()
    print(f'Alunos {alunos}\nMedia {media}')
    usuario = '.'
    while usuario not in 'SsNn':
        usuario = str(input('Dseja continuar? [S/N]:')).strip().lower()[0]
        if usuario in 'Nn':
            sair = True
print(30* '=-')

print(f'{"Nº":<6}NOME{"MÉDIA":>13}')
for c in alunos:
    count += 1
    print(f'{count}/{c[0]:^12}')

#SOLUÇÃO

alunos = []
notas = 0
sair = False

while sair == False:
    nome = str(input('Nome:')).capitalize()
    nota1 = float(input('Nota 1:'))
    nota2 = float(input('Nota 2:'))
    media = (nota1 + nota2) / 2
    alunos.append([nome,[nota1,nota2],media])
    usuario = '.'
    while usuario not in 'SsNn':
        usuario = str(input('Deseja continuar? [S/N]:')).strip().lower()[0]
        if usuario in 'Nn':
            sair = True

print(30*'=-')

print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>9}')
print(30*'-')
for p,a in enumerate(alunos):
    print(f'{p:<4}{a[0]:<10}{a[2]:>7.1f}')

print(35*"-")
while notas != 999:
    notas = int(input('Deseja mostrar a nota de qual aluno? [999 - Interrompe]:'))
    if notas <= len(alunos):
        print(f'As notas de {alunos[notas][0]} são: {alunos[notas][1]} ')
    elif notas != 999:
        print('Número incorreto, digite novamente')
    else:
        print('>>FINALIZANDO<<')
