maior = 0
menor = 0
for c in range(1, 8):
    n = int(input(f'Qual ano a {c}º pessoa nasceu?'))
    if n <= 2001:
        maior += 1
    else:
        menor += 1
print(f'{maior} pessoas atingiram a maioridade.\nEnquanto {menor} pessoas ainda são menores de idade.')

#Irá verificar a idade de 7 pessoas e dizer quais atingiram e não atingiram a maioridade.