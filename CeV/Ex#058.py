from random import randint

print(f'🔢⁉ JOGO DA ADIVINHAÇÃO! 🔢⁉')
print('Será sorteado 1 número de 0 a 10, tente adivinhar qual número foi escolhido!')

pc = randint(0, 10)
usuario = int(input('De 0 a 10, qual seu palpite?'))
acertou = usuario == pc

contador = 1

while not acertou:
    if usuario > pc:
        print('O número sorteado é menor, tente novamente.')
    else:
        print('O número sorteado é maior, tente novamente.')
    usuario = int(input('Errou, qual seu palpite?'))
    acertou = usuario == pc
    contador += 1

print(f'Você acertou, jogo foi finalizado com {contador} jogadas!')

#2 forma de fazer.

from random import randint
print('''Sou seu computador
Acabei de pensar em um número de 0 a 10.
Será que você consegue adivinhar qual foi?''')

usuario = int(input('Qual seu palpite?'))
pc = randint(0, 10)
contador = 1

while usuario != pc:
    if usuario > pc:
        usuario = int(input('Errou, o número sorteado é !MENOR!, tente de novo:'))
    else:
        usuario = int(input('Errou, o número sorteado é !MAIOR!, tente de novo:'))
    contador += 1
print(f'Você acertou! Houve {contador} tentativas! O número do jogador foi {usuario} ', end='')
print(f'e o número do computador foi {pc}. CONGRATS!!')

#3 forma de fazer.

from random import randint
print('''Sou seu computador
Acabei de pensar em um número de 0 a 10.
Será que você consegue adivinhar qual foi?''')

pc = randint(0, 10)
contador = 0
acertou = False

while not acertou:
    usuario = int(input('Qual seu palpite?'))
    contador += 1
    if usuario == pc:
        acertou = True
    else:
        if usuario < pc:
            print('Tente um número !MAIOR!')
        elif usuario > pc:
            print('Tente um número !MENOR!')
print(f'Você acertou! Houve {contador} tentativas! E o número sorteado foi {pc}.')

#Jogo da adivinhação