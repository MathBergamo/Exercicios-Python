dias = float(input('Quantos dias foram alugados? '))
km = float(input('Quantos kms foram rodados? '))
pagar = km * 0.15 + dias * 60
print(f'O preço ficou de R${pagar:.2f}')

