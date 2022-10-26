#PRIMEIRA FORMA
#nome = str(input('Digite seu nome completo: ')).strip().title()
#print('Muito prazer em te conhecer senhora(o)!')
#print(f'Seu primeiro nome é: {nome.split()[0]}')
#print(f'Seu último nome é: {nome.split()[-1]}')

n = str(input('Digite seu nome:')).title().strip()
nome = n.split()

print('Muito prazer em te conhecer')
print(f'Seu primeiro nome é: {nome[0]} \nSeu último nome é: {nome[-1]}')