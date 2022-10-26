print(10*'*=*')
print(2*" ",'SEQUÊNCIA DE FIBONACCI')
print(10*'*=*')

n = int(input('\nQuantos termos você quer mostrar?'))
t1 = t3 = 0
t2 = 1
contador = 3

print(30*'-')
print(f'{t1} -> {t2}', end='')
while contador <= n:
    t3 = t1+t2
    t1 = t2
    t2 = t3
    contador += 1
    print(f' -> {t3}', end='')
print(' [-FIM-]')
print(30*'-')

#Sequência Fiobnacci