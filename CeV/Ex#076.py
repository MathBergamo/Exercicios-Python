tupla = 'Bicicleta', 653,\
        'Capacete',129.90 ,\
        "Garrafa D'agua", 25.50,\
        'Patins', 219.90 ,\
        'Skate', 150 ,\
        'Joelheira',28 ,\
        'Cotoveleira', 23

print(45*'-')
print(f"{'LISTA DE PRODUTOS':^45}")
print(45*'-')

for produto in range(0, len(tupla)):
    if produto % 2 == 0:
        print(f'{tupla[produto]:.<25}',end='')
    elif produto % 2 == 1:
        print(f'R${tupla[produto]:.2f}')

#MODELO COM RANDINT

from random import randint
tupla = 'Caneta',(randint(9,11)),\
        'Lápis',(randint(2,4)),\
        'Borracha',(randint(4,6)),\
        'Caderno',(randint(13,19)),\
        'Papel Sulfite A4',(randint(19,29)),\
        'Agenda',(randint(15,25)),\
        'Compasso',(randint(5,13))
print(45*'=')
print(f'{"LISTA DE PRODUTOS":^40}\n{"KALUNGA":^40}')
print(45*'=')

for item in range(0, len(tupla)):
    if item % 2 == 0:
        print(f'{tupla[item]:.<30}',end='')
    elif item % 2 == 1:
        print(f'R${tupla[item]:.2f}')
print(45*'=')
print('ATENÇÃO, PREÇOS SUJEITOS A MUDANÇA')
