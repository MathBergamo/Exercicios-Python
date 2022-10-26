print(f'l{15*"*="}l\n{6*" "}MERCADINHO SALAFRAIO\nl{15*"*="}l')

total = 0
mais_barato_preco = 0
mais_barato_nome = ''
mais_de_mil = 0
continua = 's'
preco = 0
nome = ''
count = 0

while True:
    nome = str(input('Nome do produto:')).strip()
    preco = int(input('Preço: R$'))
    total += preco
    count += 1
    if preco > 1000:
        mais_de_mil += 1
    if count == 1:
        mais_barato_preco = preco
        mais_barato_nome = nome
    elif preco < mais_barato_preco:
        mais_barato_preco = preco
        mais_barato_nome = nome
    continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while continua not in 'sS' and continua not in 'Nn':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]

    if continua in 'Nn':
        break
print(f'O total gasto foi R${total}\nTemos {mais_de_mil} produtos que custam mais de R$1000.00\nO produto ', end='')
print(f'mais barato é a(o) {mais_barato_nome} custando R${mais_barato_preco}')

