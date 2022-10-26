a = input('Digite algo: ')
print('O tipo primitivo é: ', type(a))
print('É númerico?', a.isnumeric())
print('É alfanumérico? ', a.isalnum())
print('É alfabético? ', a.isalpha())
print('Contém apenas espaço? ', a.isspace())
print('É capitalizado? ', a.istitle())
print('Contém apenas letras maiúsculas? ', a.isupper())
print('Contém apenas letras minúsculas? ', a.islower())

input('Primeira parte com virgula: ok!, pressione enter para a próxima parte')

print(f'O tipo primitivo é: {type(a)}')
print(f'É númerico? {a.isnumeric()}')
print(f'É alfanumérico? {a.isalnum()}')
print(f'É alfabético? {a.isalpha()}')
print(f'Contém apenas espaço? {a.isspace()}')
print(f'É capitalizado? {a.istitle()}')
print(f'Contém apenas letras maiúsculas? {a.isupper()}')
print(f'Contém apenas letras minúsculas? {a.islower()}')

input('''Parte final:
Parabéns, você conseguiu :)''')
