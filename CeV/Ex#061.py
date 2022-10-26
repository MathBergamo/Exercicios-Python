print('DETECTOR DE PA')
t1 = int(input('Digite o primeiro termo: '))
rz = int(input('Digite a razão: '))
contador = 0

while contador != 10:
    print(t1, end=' > ')
    t1 += rz
    contador += 1

#Progressão aritmética com while