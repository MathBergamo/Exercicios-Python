maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}º Pessoa:  '))
    if c == 1:
        maior = peso
        menor = peso
    if peso > maior:
        maior = peso
    if peso < menor:
            menor = peso
print(f'A pessoa com maior peso tem {maior}\nEnquanto a de menor peso tem {menor}')

#Identifica o maior e o menor peso