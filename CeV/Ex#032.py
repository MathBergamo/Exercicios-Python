from datetime import date

ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
    print(f'{ano}')
if ano % 400 == 0 and ano % 4 == 0 or ano % 100 != 0: #formula para identificar o ano bissexto
    print('O ano é BISSEXTO!')
else:
    print('O ano não é BISSEXTO')

#Irá dizer se o ano é ou não é bissexto