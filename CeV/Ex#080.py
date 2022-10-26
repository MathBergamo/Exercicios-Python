#1 ALTERNATIVA

lista = []
for c in range(5):
    n = int(input("Digite o numero: "))
    if c == 0 or n > lista[-1]:
        lista.append(n)
    else:
        for pos, x in enumerate(lista):
            if n <= x:
                lista.insert(pos, n)
                break
print(lista)

#2 ALTERNATIVA

lista = []

for c in range(0, 5):
    n = int(input('Digite um número:'))
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print(f'Adicionado no final da lista')
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                print(f'Adicionado na posição {pos}')
                break
            pos += 1
print(f'\nA lista ordenada dos números é: {lista}')
