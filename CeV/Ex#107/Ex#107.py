import moeda

p = float(input('Digite um preço: R$'))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando em 10% temos: R${moeda.aumentar(p)}')
print(f'Reduzindo em 13% temos: R${moeda.diminuir(p)}')
