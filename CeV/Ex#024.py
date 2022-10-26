cidade = str(input('Digite o nome de uma cidade:')).lower().strip()
santo = cidade.split()[0]
print('santo' in santo)

#Irá apresentar valor boleano caso True ou False caso 'santo' esteja no parâmetro 0 da variávvel santo.