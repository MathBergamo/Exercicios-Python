# PRIMEIRA TENTATIVA

print('GERADOR DE PA')

t1 = int(input('Primeiro termo:'))
rz = int(input('Razão:'))
count = 0
usuario = 1
total = 10
while usuario != 0:
    while count <= total:
        print(t1, '> PAUSA' if count == total else '> ', end='')
        t1 += rz
        count += 1
    usuario = int(input('\n\nQuer mostrar mais termos? [0 - Parar]'))
    total = usuario - 1
    count = 0
print('FIM')


#FINAL

print('PROGRESSÃO ARITMÉTICA V3.0')
t1 = int(input('Digite o primeiro termo:'))
rz = int(input('Digite a razão:'))

contador = 1
total = 0
mais = 10

while mais != 0:
    total = total + mais
    while contador <= total:
        print(f'{t1}', end=' > ')
        t1 += rz
        contador += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mais?'))
print('FIM')

#Progressão Aritmética V3.0