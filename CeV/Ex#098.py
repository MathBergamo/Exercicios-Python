def contador(inicio, fim, passo):
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = abs(passo)
    if inicio > fim:
        passo = -passo
        fim -= 2
    for c in range(inicio, fim+1, passo):
        print(c, end = ' ')
    print()


contador(1,10,0)
contador(10,0,2)
contador(int(input('Digite o ínicio: ')), int(input('Ditite o fim: ')), int(input('Digite o passo: ')))

# precisa transformar em positivo para caso o usuario digitar um valor negativo. ( valor negativo com valor negativo
# Transforma o valor em positivo, logo, não é possível fazer uma contagem decrescente. )
# O valor irá se tornar negativo em caso da contagem precisar decrescer ( If inicio > fim ), ou seja, com o inicio maior que o fim
# Exemplo: 20 para 0 contando de 1 ou -1

#PRIMEIRA TENTATIVA
from time import sleep

def contador(i,f,p):
    print(20*'-=')
    print(f'Contagem de 1 a 10 de 1 em 1')
    for c in range(1,11):
        sleep(0.4)
        print(c,end=' ')
    print()
    print(20 * '-=')
    print(f'Contagem de 10 até 0 de 2 em 2')
    for c in range(10,-1,-2):
        sleep(0.4)
        print(c,end=' ')
    print()
    print(20 * '-=')
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for c in range(i,f,p):
        sleep(0.4)
        print(c,end=' ')

contador(int(input('Inicío:')),int(input('Fim:')),int(input('Passo:')))
