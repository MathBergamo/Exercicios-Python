print(5*"==-", 'Lojinhas Mateto', 5*"-==")

preco = float(input('Digite o valor à ser pago R$'))

print('''DIGITE A FORMA DE PAGAMENTO
[1] - À vista no dinheiro/cheque
[2] - À vista no cartão
[3] - 2x no cartão
[4] - 3x ou mais no cartão.''')
opcao = int(input('Qual a forma de pagamento?'))

if opcao == 1:
    print(f'O valor à ser pago de R${preco} agora sairá no valor de R${preco - preco*0.10} com 10% de desconto!')
elif opcao == 2:
    print(f'O valor à ser pago de R${preco} agora sairá no valor de R${preco - preco*0.05} com 5% de desconto!')
elif opcao == 3:
    print(f'O valor à ser pago de R${preco} ficará dividído em 2x parcelas de R${preco/2} não há alteração no', end=' ')
    print('preço final!')
elif opcao == 4:
    parcelas = float(input('Quantas parcelas serão?'))
    print(f'O preço de cada parcela sairá no valor de R${(preco+preco*0.20) / parcelas:.2f}')
    print(f'O valor à ser pago de R${preco} agora sairá no valor de R${preco + preco*0.20} com acréscimo de 20%')
else:
    print('Opção inválida, tente novamente!')
print(4*"*=", 'Muito obrigado! :)', 4*"=*")

#Irá calcular o preço a se pagar de acordo com a forma de pagamento