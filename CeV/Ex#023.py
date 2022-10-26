num = int(input('Digite um número com até 4 digitos: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Unidade: {u}')
print(f'Dezena: {d}')
print(f'Centena: {c}')
print(f'Milhar: {m}')

#Divisão inteira converte o valor para número inteiro.
# O resto da divisão por 10 permite pegar apenas 1 número do resultado da divisão.