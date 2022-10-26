from random import choice
a1 = str(input('Digite o nome do aluno: ')).strip()
a2 = str(input('Digite o nome do aluno: ')).strip()
a3 = str(input('Digite o nome do aluno: ')).strip()
a4 = str(input('Digite o nome do aluno: ')).strip()

lista = choice([a1,a2,a3,a4])
print(f'O Aluno sorteado foi {lista}')

#Choice irá escolher apenas um dos valores da lista