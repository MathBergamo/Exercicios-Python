n_inteiro = int(input('Digite um número: '))

print('''[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')

opcao = int(input('Sua opção: '))

if opcao == 1:
    print(f'{n_inteiro} Convertido para BINÁRIO é:{(bin(n_inteiro))[2:]}')
elif opcao == 2:
    print(f'{n_inteiro} Convertido para OCTAL é:{(oct(n_inteiro))[2:]} ')
elif opcao == 3:
    print(f'{n_inteiro} Convertido para HECADECIMAL é: {hex(n_inteiro)[2:]}')
else:
    print('Opção inválida, tente novamente:')

#conversão dos números para binário, octal e hexadecimal