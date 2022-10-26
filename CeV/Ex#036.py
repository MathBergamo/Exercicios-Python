casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
anos = float(input('Digite em quantos anos você quer financiar:'))

prestacao = casa / (12*anos)
maximo = salario *30/100

print(f'O valor máximo para o financiamento em {anos:.0f} anos com base em seu salário é de R${maximo} e o valor da prestação é R${prestacao:.2f}')

if maximo >= prestacao:
    print('Seu financiamento foi aprovado! :)')
else:
    print('Seu financiamento foi negado! =c')

#Caso a prestação seja maior que 30% do salário do usuario, o financiamento é negado.

#2 opção
#casa = float(input('Digite o valor da casa R$'))
#salario = float(input('Digite o valor do salário R$'))
#anos = int(input('Em quantos anos você pretende pagar? '))

#prestacao = casa / (12*anos)

#print(f'Para pagar a casa de R${casa} em {anos} anos, O valor das parcelas mensais será equivalente a R${prestacao:.2f}')

#if prestacao < salario * 0.30:
    #print(f'Empréstimo concebido! o valor máximo para seu empréstimo é de {salario * 0.30}')
#else:
    #print(f'Empréstimo negado! O valor máximo para seu financiamento mensal é de {salario * 0.30}')
