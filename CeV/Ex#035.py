print('=-='*20)
print(15*' ' , 'Digite o valor das retas:')
print('=-='*20)

r1 = float(input('Primeira reta: '))
r2 = float(input('Segunda reta: '))
r3 = float(input('Terceira reta: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('É possível formar um triângulo com essa três retas.')
else:
    print('Não é possível formar um triângulo com essas três retas.')

#Fórmula para formar um triângulo: nenhuma reta pode ser maior que a soma das outras duas restantes.