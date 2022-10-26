frase = str(input('Digite uma frase: ')).strip().upper().split()
junto = ''.join(frase)
inverso = ''

for c in range(len(junto) -1, -1, -1):
    inverso += junto[c]
if inverso == junto:
    print(f'Temos um palíndromo! {inverso} é igual a {junto}')
else:
    print('A frase digitada não é um palíndromo')

#2 forma de fazer com replace

frase = str(input('Digite uma frase: ')).strip().upper().replace(' ', '')
inverso = ''
for c in range(len(frase)-1, -1, -1):
    inverso += frase[c]
if inverso == frase:
    print(f'As palavras {frase} e {inverso} são um palíndromo')
else:
    print(f'As palavras {frase} e {inverso} não são um palíndromo')

#Verifica se a frase é um palíndromo.