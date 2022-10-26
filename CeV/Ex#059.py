from time import sleep
print('''✖➕ MENU DE CONCEITOS MATEMÁTICOS! ➕✖
    ---  Digite dois valores  ---''')

n1 = int(input('Primeiro valor:'))
n2 = int(input('Segundo valor:'))
usuario = 0
while usuario != 5:
    usuario = int(input('''\n[1] - Somar
[2] - Multiplicar
[3] - Maior
[4] - Novos números
[5] - Sair do programa

Escolha uma das opções: '''))
    if usuario == 1:
        print(f'\nA soma de {n1} + {n2} = {n1+n2}')
        sleep(1)
    elif usuario == 2:
        print(f'\nA multiplicação de {n1} x {n2} = {n1*n2}')
        sleep(1)
    elif usuario == 3:
        if n1 > n2:
            print(f'\nO maior número entre {n1} e {n2} é [{n1}]')
            sleep(1)
        elif n2 > n1:
            print(f'\nO maior número entre {n2} e {n1} é [{n2}]')
            sleep(1)
    elif usuario == 4:
        n1 = int(input('\nDigite o novo primeiro valor:'))
        n2 = int(input('Digite o novo segundo valor:'))
        print('Colocando números novos...')
        sleep(1)
    elif usuario == 5:
        print('Finalizando programa...')
        sleep(1)
        print('Volte sempre!')
    else:
        print('Opção inválida, tente novamente:')

#Menu com opções de operações matemáticas