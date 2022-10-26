print('Controle de Terrenos')
print(25*'-')
def area(larg,comp):
    a = larg * comp
    print(f'A área do terreno de {l:.1f}x{c:.1f} é de {a:.1f}m². ')

l = float(input('Largura (M):'))
c = float(input('Comprimento (M):'))
area(l,c)
