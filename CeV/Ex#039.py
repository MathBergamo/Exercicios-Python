idade = int(input('Quantos anos você tem? '))

if idade < 18:
    print('Você ainda irá se alistar futuramente.')
    print(f'Faltam {18-idade} ano(s) para você se alistar')
elif idade == 18:
    print('Você está na hora de morfar (é brincks vai se alistar).')
    print(f'Faltam {18-idade} é só isso, não tem mais jeito, acabou, boa sorte.')
else:
    print('Veião, serviu? então passou, cu doce!')
    print(f'Faz {idade-18} ano(s) que tu serviu ou tinha que servir putão')

#Verificador de alistamento de acordo com a idade