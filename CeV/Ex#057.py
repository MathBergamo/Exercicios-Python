sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Digitação errada, tente novamente!')
    sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
print('Sexo registrado.')

#Irá requisitar o sexo do usuario até o mesmo digitar da forma certa de acordo com a exigência da estrutura while.