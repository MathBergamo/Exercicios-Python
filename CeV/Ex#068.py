#Primeira tentativa de solução!
from random import randint
print('🖖 =- 🤜 [PAR OU IMPAR] 🤛 -= 🖖')


usuario = int(input('Escolha um número de 0 a 10: '))
impar_par = str(input('Ímpar ou par? [I/P]')).upper().strip()[0]
while impar_par not in 'IiPp':
    impar_par = str(input('Ímpar ou par? [I/P]')).upper().strip()[0]

computador = randint(1, 10)
count = 0
resultado_n = computador+usuario
resultado_impar_par = ''

while True:
    if resultado_n % 2 == 1 and impar_par in 'Ii':
        resultado_impar_par = 'ÍMPAR'
        count += 1
        print(f'Você jogou {usuario} e o computador jogou {computador}. O número total de {resultado_n} é {resultado_impar_par}!  ')
        usuario = int(input('Você venceu!\nVamos jogar de novo..\n\nEscolha um número de 0 a 10: '))
        impar_par = str(input('Ímpar ou par? [I/P]')).upper().strip()[0]
        while impar_par not in 'IiPp':
            impar_par = str(input('Ímpar ou par? [I/P]')).upper().strip()[0]
        computador = randint(1, 10)
        resultado_n = computador + usuario
    elif resultado_n % 2 == 0 and impar_par in "Pp":
        resultado_impar_par = 'PAR'
        count += 1
        print(f'Você jogou {usuario} e o computador jogou {computador}. O número total de {resultado_n} é {resultado_impar_par}!')
        usuario = int(input('Você venceu!\nVamos jogar de novo..\n\nEscolha um número de 0 a 10: '))
        impar_par = str(input('Ímpar ou par? [I/P]')).upper().strip()[0]
        while impar_par not in 'IiPp':
            impar_par = str(input('Ímpar ou par? [I/P]')).upper().strip()[0]
        computador = randint(1, 10)
        resultado_n = computador + usuario
    else:
        resultado_impar_par = resultado_impar_par
        break
print(f'Você perdeu!\n{20*"-="}\nVocê digitou {usuario} e o computador {computador}. A soma é {resultado_n}', end='')
print(f' e o valor é {resultado_impar_par}. Você acumulou {count} vitórias!')

#Solução final

from random import randint
count = 0

while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = jogador + computador
    tipo = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    while tipo not in 'PpIi':
        tipo = str(input('Par ou Ímpar? [P/I]')).upper().strip()[0]
    print(f'Você jogou {jogador} e o computador {computador}', end='')
    print(f'\nDEU PAR!' if total % 2 == 0 else '\nDEU ÍMPAR!')
    if tipo in 'Pp':
        if total % 2 == 0:
            print(f'\nVocê GANHOU!')
            count += 1
        else:
            print('\nVocê PERDEU!')
            break
    elif tipo in 'Ii':
        if total % 2 == 1:
            print(f'\nVocê GANHOU')
            count += 1
        else:
            print('\nVocê PERDEU!')
            break
    print('Vamos jogar de novo...')
print(f'\nFIM DE JOGO!\nVocê venceu {count}x vezes')

