from datetime import date
ano = int(input('Qual ano o atleta nasceu? '))
idade = date.today().year - ano

if idade <= 9:
    print(f'O atleta tem {idade} está na categoria: \n{5*":-:"}MIRIM{5*":-:"}')
elif 9 < idade <= 14:
    print(f'O atleta tem {idade} está na categoria: \n{5*":-:"}INFANTIL{5*":-:"}')
elif 14 < idade <= 19:
    print(f'O atleta tem {idade} está na categoria: \n{5*":-:"}JUNIOR{5*":-:"}')
elif 19 < idade <= 25:
    print(f'O atleta tem {idade} está na categoria: \n{5*":-:"}SÊNIOR{5*":-:"}')
elif 25 < idade:
    print(f'O atleta tem {idade} está na categoria: \n{5*":-:"}MASTER{5*":-:"}')
else:
    print('Algo deu errado, tente novamente.')

#Irá verificar a categoria do atleta de acordo com a idade