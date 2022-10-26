soma_da_idade = 0
media = 0
maior_idade_homem = 0
nome_mais_velho = ''
mulheres_menos_vinte = 0

for c in range(1, 5):
    print(f'----{c}º PESSOA----')
    nome = str(input('Nome:')).capitalize().strip()
    idade = int(input('Idade:'))
    sexo = str(input('Sexo [M/F]')).upper().strip()
    soma_da_idade += idade
    if idade < 20 and sexo in 'Ff':
        mulheres_menos_vinte += 1
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
media = soma_da_idade/4

print(f'A média de idade de todas as pessoas é de {media}')
print(f'O homem mais velho se chama {nome_mais_velho}, e ele tem {maior_idade_homem} anos')
print(f'Há {mulheres_menos_vinte} mulheres com menos de 20 anos.')

#Apresenta informações coletadas pela estrutura de repetição.