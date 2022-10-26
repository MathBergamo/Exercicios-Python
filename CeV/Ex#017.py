from math import hypot
co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(ca , co)

print(f'A hipotenusa é: {hi:.2f}')

#PRIMEIRA SOLUÇÃO

#co = float(input('Comprimento do cateto oposto: '))
#ca = float(input('Comprimento do cateto adjacente: '))
#hi = (co ** 2 + ca ** 2) ** (1/2)
#print(f'A hipotenusa irá medir {hi:.2f}')
