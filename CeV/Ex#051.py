print(25*'=')
print('  PROGRESSÃO ARITMÉTICA  ')
print(25*'=')

n = int(input('\nDigite um número: '))
r = int(input('Digite a razão: '))

for c in range (n , n+10*r, r):
    print(c, end = ' > ')

#2 alternativa para resolver

p1 = int(input('Primeiro termo: '))
rz = int(input('Razão: '))
for c in range(0, 10,):
    print(f'{p1 + rz * c}', end = ' > ')

#3 alternativa para resolver

t1 = int(input('termo inicial'))
r = int(input('razao'))

for i in range(0,10):
    print(t1)
    t1 += r

#Progressão aritimética