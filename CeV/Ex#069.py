print('--- ANALISADOR DE CADASTROS ---')

total_maior = homens = mulheres_menos20 = idade = 0
continua = ''
sexo = ''

while True:
    print('\n--- CADASTRO ---')
    idade = int(input('Idade:'))
    while idade <= 0:
        idade = int(input('Idade:'))
    sexo = str(input('Sexo [F/M]')).upper().strip()[0]
    while sexo not in 'Ff' and sexo not in 'Mm':
        sexo = str(input('Sexo [F/M]')).upper().strip()[0]
    continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    while continua not in 'Ss' and continua not in 'Nn':
        continua = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if idade >= 18:
        total_maior += 1
    if sexo in 'Mm':
        homens += 1
    elif sexo in 'Ff' and idade < 20:
        mulheres_menos20 += 1
    if continua in 'Nn':
        break
print(f'Temos {total_maior} pessoas maiores de 18 anos\nForam cadastrados {homens} homens.\n', end='')
print(f'E temos {mulheres_menos20} mulher(es) com menos de 20 anos.')

